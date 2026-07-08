company_map = {

    "apple": "AAPL",
    "tesla": "TSLA",
    "nvidia": "NVDA",
    "microsoft": "MSFT",
    "google": "GOOGL",
    "alphabet": "GOOGL",
    "amazon": "AMZN",
    "meta": "META",
    "facebook": "META",
    "netflix": "NFLX",
    "amd": "AMD",
    "intel": "INTC",
    "goldman sachs": "GS",
    "jpmorgan": "JPM",
    "j.p. morgan": "JPM",
    "berkshire hathaway": "BRK-B"

}


def get_ticker(company):

    company = company.lower().strip()


    if company in company_map:

        return company_map[company]


    # if user already entered ticker
    return company.upper()