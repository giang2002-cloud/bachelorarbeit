import requests
from bs4 import BeautifulSoup

url = "https://www.srnav.com/reports"
response = requests.get(url)
response.raise_for_status()
soup = BeautifulSoup(response.text, "html.parser")

# Find all rows (adjust class as needed)
container = soup.find("div", class_="col-span-full row-span-1 row-start-2 grid h-fit grid-cols-subgrid")
if container:
    rows = container.find_all("div", class_="cursor-grab")
    print(f"Found {len(rows)} rows")
    for row in rows:
        print(row.get_text(strip=True))
else:
    print("Container not found")
    
for row in rows:
    # Company
    company = row.find("span", class_="text-xs font-medium")
    company_name = company.get_text(strip=True) if company else ""
    print(company_name)

    # All <span> with border-primary-white-100 are data columns
    columns = row.find_all("span", class_="border-primary-white-100 group flex items-center border-l px-3 text-xs font-medium")
    col_texts = [col.get_text(strip=True) for col in columns]
    print(col_texts)
    # Pages (look for <a> tags inside the hidden md:flex div)
    pages_div = row.find("div", class_="hidden md:flex")
    page_links = []
    if pages_div:
        page_links = [a['href'] for a in pages_div.find_all("a", href=True)]

    # Total Pages (look for <span> inside hidden text-sm md:flex)
    total_pages = ""
    total_pages_div = row.find("div", class_="hidden text-sm md:flex")
    if total_pages_div:
        total_pages_span = total_pages_div.find("span")
        if total_pages_span:
            total_pages = total_pages_span.get_text(strip=True)

    # Output the extracted data
    print({
        "Company": company_name,
        "Country": col_texts[0] if len(col_texts) > 0 else "",
        "Sector": col_texts[1] if len(col_texts) > 1 else "",
        "Industry": col_texts[2] if len(col_texts) > 2 else "",
        "Page Links": page_links,
        "Total Pages": total_pages,
        "Auditor": col_texts[3] if len(col_texts) > 3 else "",
        "Published": col_texts[4] if len(col_texts) > 4 else "",
    })