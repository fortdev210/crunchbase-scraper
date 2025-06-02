import requests
import json

from config import email, password

def get_user_session(email: str, password: str):
    url = "https://www.crunchbase.com/v4/cb/sessions"

    payload = json.dumps({
        "email": email,
        "password": password
    })

    headers = {'Content-Type': 'application/json'}
    response = requests.request("POST", url, headers=headers, data=payload)

    if response.status_code == 201:
        print("User session created successfully.")
        
        # Get cookies from the response
        cookies = response.cookies
      
        return cookies

    else:
        print("Failed to create user session.", response.status_code, response.text)
        return None 
        
def get_organization(cookies, company:str):
    url = f"https://www.crunchbase.com/v4/data/entities/organizations/{company}/overrides"

    params = {
        "field_ids": [
            "identifier", "layout_id", "facet_ids", "title", "short_description",
            "is_locked", "rank_delta_d90", "investor_identifiers"
        ],
        "card_ids": [
            "aberdeen_attribution", "acquisition_prediction", "company_about_fields1",
            "apptopia_app_rating_list", "apptopia_sdk_list", "apptopia_attribution",
            "bombora_attribution", "builtwith_tech_not_used_headline",
            "builtwith_tech_not_used_list", "builtwith_attribution",
            "company_about_fields2", "growth_and_heat", "company_financials_highlights",
            "funding_prediction", "growth_prediction", "ipqwery_attribution",
            "ipqwery_patents_by_category_chart", "ipqwery_patents_headline",
            "ipqwery_patents_list", "ipqwery_trademark_headline",
            "ipqwery_trademark_list", "ipqwery_trademarks_by_class_chart",
            "org_category_ranks", "people_highlights", "semrush_overview_headline",
            "semrush_overview", "semrush_attribution", "siftery_product_status_list",
            "siftery_product_create_list", "siftery_attribution", "ipo_prediction",
            "awards", "legal_proceedings", "offices", "partnership_announcements",
            "product_launches"
        ]
    }

    payload = json.dumps({
      "card_lookups": [
        {
          "card_id": "org_similarity_list",
          "limit": 20
        }
      ]
    })

    headers = {
      'Content-Type': 'application/json',
      'Cookie': '; '.join([f'{cookie.name}={cookie.value}' for cookie in cookies]),
    }

    response = requests.post(url, headers=headers, params=params, data=payload)
    
    data = json.loads(response.text)
    
     # Company details
    identifier = data.get("properties", {}).get("identifier", {})
    company_name = identifier.get("value")
    company_uuid = identifier.get("uuid")
    permalink = identifier.get("permalink")

    print(f"🗂️ Company Name: {company_name}")
    print(f"🔗 Permalink: {permalink}")
    print(f"🔑 UUID: {company_uuid}\n")

    # Similar companies
    similar_companies = data.get("cards", {}).get("org_similarity_list", [])

    for company in similar_companies:
        print("📦 Similar Company:")
        target = company.get("target", {})
        print(f"  - Name: {target.get('value')}")
        print(f"  - Permalink: {target.get('permalink')}")
        print(f"  - Short Description: {company.get('target_short_description')}")
        print(f"  - Revenue Range: {company.get('target_revenue_range', 'N/A')}")
        print(f"  - Employee Range: {company.get('target_num_employees_enum', 'N/A')}")

        # Categories
        categories = company.get("target_categories", [])
        category_names = [cat.get("value") for cat in categories]
        print(f"  - Categories: {', '.join(category_names)}\n")

if __name__ == "__main__":
    cookies = get_user_session(email=email, password=password)
    
    if cookies:
      get_organization(cookies=cookies, company="openai")