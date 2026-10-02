from fastapi import FastAPI, Query, HTTPException

from catalogue_model import *

MOCK_SERVICES = [
    {
        "id": "surf-node:servicebundle:nl-research-portal",
        "abbreviation": "NLRP",
        "name": "Netherlands Research Portal",
        "webpage": "https://netherlands.openaire.eu/",
        "description": "A comprehensive collection of Dutch open research information, covering publications, research data sets, and research software items from Dutch repositories and CRIS systems, linked to research grants and research-performing organisations across the Netherlands.",
        "tagline": "Discover Dutch open research outputs",
        "logo": "https://www.surf.nl/themes/surf/logo.svg",
        "scientificDomains": [
            {
                "scientificDomain": "scientific_domain-generic"
            }
        ],
        "categories": [
            {
                "category": "service_classification-publishing_discovery"
            }
        ],
        "targetUsers": [
            "target_user-research_communities",
            "target_user-research_groups",
            "target_user-research_projects",
            "target_user-researchers",
            "target_user-policy_makers",
            "target_user-innovators",
            "target_user-other",
            "target_user-funders",
            "target_user-businesses"
        ],
        "accessModes": ["access_mode-free"],
        "tags": [
            "catalogue",
            "metadata",
            "netherlands",
            "openaire",
            "research"
        ],
        "languageAvailabilities": [
            "EN"
        ],
        "helpdeskEmail": "servicedesk@surf.nl",
        "securityContactEmail": "info@surf.nl",
        "trl": "trl-8",
        "userManual": "https://netherlands.openaire.eu/content",
        "termsOfUse": "https://www.openaire.eu/terms-of-use",
        "privacyPolicy": "https://www.openaire.eu/privacy",
        "accessPolicy": "https://netherlands.openaire.eu/",
        "orderType": "order_type-open_access"
    },
    {

        "id": "surf-node:servicebundle:research-drive",
        "abbreviation": "RD",
        "name": "Research Drive",
        "webpage": "https://www.surf.nl/en/services/storage-data-management/research-drive",
        "description": "Does your research team need a lot of storage capacity for research data? Are you working with other institutions, industry or international partners? Research Drive allows you to store and share your research data in an online environment.",
        "tagline": "Secure and flexible collaboration",
        "logo": "https://www.surf.nl/themes/surf/logo.svg",
        "scientificDomains": [
            {
                "scientificDomain": "scientific_domain-engineering_and_technology"
            }
        ],
        "categories": [
            {
                "category": "service_classification-storage_services"
            }
        ],
        "targetUsers": [
            "target_user-research_communities",
            "target_user-research_groups",
            "target_user-research_projects",
            "target_user-researchers"
        ],
        "accessModes": ["access_mode-other"],
        "tags": [
            "drive",
            "research",
            "storage-data-management",
            "surf"
        ],
        "languageAvailabilities": [
            "EN",
            "NL"
        ],
        "helpdeskEmail": "servicedesk@surf.nl",
        "securityContactEmail": "info@surf.nl",
        "trl": "trl-8",
        "userManual": "https://www.surf.nl/en/services/storage-data-management/research-drive",
        "termsOfUse": "https://www.surf.nl/en/terms-and-conditions",
        "privacyPolicy": "https://www.surf.nl/en/privacy-statement",
        "accessPolicy": "https://servicedesk.surf.nl",
        "orderType": "order_type-order_required"

    },
    {

        "id": "surf-node:servicebundle:surf-research-cloud",
        "abbreviation": "SRC",
        "name": "SURF Research Cloud",
        "webpage": "https://eosc.nl",
        "description": "SURF Research Cloud is a portal where you easily build a virtual research environment. You can use preconfigured workspaces and datasets or add them yourself. Institutions, research communities and suppliers can contribute to Research Cloud's functionality and catalogue by integrating their computing and data services.",
        "tagline": "Create reproducible research environments",
        "logo": "https://www.surf.nl/themes/surf/logo.svg",
        "scientificDomains": [
            {
                "scientificDomain": "scientific_domain-generic"
            }
        ],
        "categories": [
            {
                "category": "service_classification-compute_services"
            },
            {
                "category": "service_classification-compute_services"
            },
            {
                "category": "service_classification-compute_services"
            },
            {
                "category": "service_classification-storage_services"
            },
            {
                "category": "service_classification-storage_services"
            },
            {
                "category": "service_classification-science_gateways"
            }
        ],
        "targetUsers": [
            "target_user-providers",
            "target_user-research_communities",
            "target_user-research_groups",
            "target_user-research_infrastructure_managers",
            "target_user-research_organisations",
            "target_user-research_projects",
            "target_user-researchers",
            "target_user-students"
        ],
        "accessModes": ["access_mode-free"],
        "tags": [
            "cloud",
            "compute",
            "research",
            "surf"
        ],
        "languageAvailabilities": [
            "EN"
        ],
        "helpdeskEmail": "servicedesk@surf.nl",
        "securityContactEmail": "cert@surfcert.nl",
        "trl": "trl-9",
        "userManual": "https://servicedesk.surf.nl/wiki/spaces/WIKI/pages/9798172/SURF+Research+Cloud",
        "termsOfUse": "https://servicedesk.surf.nl/wiki/spaces/WIKI/pages/17825957/SRC+Acceptable+Use+Policy",
        "privacyPolicy": "https://www.surf.nl/en/privacy-statement",
        "accessPolicy": "https://www.surf.nl/en/access-to-compute-services",
        "orderType": "order_type-order_required"

    },
    {
        "id": "surf-node:servicebundle:surffilesender",
        "abbreviation": "S",
        "name": "SURFfilesender",
        "webpage": "https://www.surf.nl/en/services/storage-data-management/surffilesender",
        "description": "Send files securely and encrypted. With SURFfilesender, you send large files, such as research data, with confidence. The files are stored in the Netherlands. Encryption offers extra security.",
        "tagline": "Send and receive files easily",
        "logo": "https://www.surf.nl/themes/surf/logo.svg",
        "scientificDomains": [
            {
                "scientificDomain": "scientific_domain-engineering_and_technology"
            }
        ],
        "categories": [
            {
                "category": "service_classification-storage_services"
            }
        ],
        "targetUsers": [
            "target_user-research_communities",
            "target_user-research_groups",
            "target_user-research_projects",
            "target_user-researchers"
        ],
        "accessModes": ["access_mode-free"],
        "tags": [
            "storage-data-management",
            "surf",
            "surffilesender"
        ],
        "languageAvailabilities": [
            "EN",
            "NL"
        ],
        "helpdeskEmail": "info@surf.nl",
        "securityContactEmail": "info@surf.nl",
        "trl": "trl-8",
        "userManual": "https://www.surf.nl/en/services/storage-data-management/surffilesender",
        "termsOfUse": "https://www.surf.nl/en/terms-and-conditions",
        "privacyPolicy": "https://www.surf.nl/en/privacy-statement",
        "accessPolicy": "https://filesender.surf.nl/",
        "orderType": "order_type-open_access"
    }

]

# --- FastAPI App ---
app = FastAPI(title="Service Catalogue API", version="2.0.0")


# --- Endpoint: GET /services ---
@app.get(
    "/services",
    response_model=PagingServiceBundle,
    responses={
        400: {
            "model": HTTPError,
            "description": "Invalid query parameters (quantity, from, order or sort)",
        }
    },
)
async def get_services(
        keyword: Optional[str] = Query(None, description="Keyword to refine the search"),
        from_: Optional[int] = Query(0, description="Starting index in the result set (0-based)", alias="from"),
        quantity: Optional[int] = Query(10, description="Number of results to fetch (default 10)"),
        order: Optional[str] = Query("asc", description="Order of results: 'asc' or 'desc'"),
        sort: Optional[str] = Query("name", description="Field to sort by: 'name', 'description', 'total' (by ID)")
):
    """
    Get a list of Service profiles based on filters.

    Params:
        keyword: String (optional) – keyword to filter on name, description, tags
        from: String (optional) – starting index (0-based), default 0
        quantity: String (optional) – number of results to return, default 10
        order: String (optional) – 'asc' or 'desc', default 'asc'
        sort: String (optional) – field to sort by: 'name', 'description', 'id'

    Example:
        GET /services?quantity=50&keyword=data
    """

    # Validate inputs
    if quantity <= 0:
        raise HTTPException(status_code=400, detail="quantity must be > 0")
    if from_ < 0:
        raise HTTPException(status_code=400, detail="from must be >= 0")

    # Convert sort field to lowercase
    sort = sort.lower()
    order = order.lower()

    # Validate sort field
    valid_sort_fields = {"name", "description", "id", "total"}
    if sort not in valid_sort_fields:
        raise HTTPException(
            status_code=400,
            detail=f"sort must be one of: {', '.join(valid_sort_fields)}"
        )

    # Validate order
    if order not in {"asc", "desc"}:
        raise HTTPException(status_code=400, detail="order must be 'asc' or 'desc'")

    # Build search results
    results = []
    matched_count = 0
    skip = from_

    for item in MOCK_SERVICES:
        # Apply keyword filter
        if keyword:
            keyword_lower = keyword.lower()
            if not (
                    keyword_lower in item["name"].lower()
                    or keyword_lower in item["description"].lower()
                    or any(keyword_lower in tag.lower() for tag in item.get("tags", []))
            ):
                continue

        # Build Service object
        service = Service(
            id=item["id"],
            alternativeIdentifiers=[
                AlternativeIdentifier(type=alt_id["type"], value=alt_id["value"])
                for alt_id in item.get("alternativeIdentifiers", [])
            ],
            abbreviation=item.get("abbreviation", None),
            name=item["name"],
            description=item["description"],
            tags=item.get("tags", item["tags"]),
            tagline=item["tagline"],
            logo=item["logo"],
            languageAvailabilities=item["languageAvailabilities"],
            orderType=OrderType(item["orderType"]),
            scientificDomains=[
                ServiceProviderDomain(scientificDomain=ScientificDomain(domain["scientificDomain"]))
                for domain in item["scientificDomains"]
            ],
            categories=[
                ServiceCategory(category=Category(cat["category"]))
                for cat in item["categories"]
            ],
            targetUsers=[
                TargetUser(user)
                for user in item["targetUsers"]
            ],
            webpage=item["webpage"],
            accessModes=[
                AccessMode(am)
                for am in item["accessModes"]
            ],
            securityContactEmail=item["securityContactEmail"],
            trl=TRL(item["trl"]),
            helpdeskEmail=item["helpdeskEmail"],
            userManual=item["userManual"],
            termsOfUse=item["termsOfUse"],
            privacyPolicy=item["privacyPolicy"],
            accessPolicy=item["accessPolicy"]
        )

        # Add to results
        results.append(ServiceBundle(id=item["id"], service=service))
        matched_count += 1

    # Sort results
    def get_sort_key(item: ServiceBundle):
        if sort == "name":
            return item.service.name.lower()
        elif sort == "description":
            return item.service.description.lower()
        elif sort == "id":
            return item.id.lower()
        return 0

    results.sort(key=get_sort_key, reverse=(order == "desc"))

    # Apply pagination
    to_index = from_ + quantity
    paginated_results = results[from_:to_index]

    # Return response
    return PagingServiceBundle.model_validate({
        "total": matched_count,
        "from": from_,
        "to": from_ + len(paginated_results),
        "results": paginated_results
    })
