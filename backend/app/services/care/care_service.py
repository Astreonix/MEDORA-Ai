from dataclasses import asdict, dataclass


@dataclass(frozen=True)
class CareProvider:
    id: str
    name: str
    specialty: str
    location: str
    visit_type: str = "Contact provider"
    cost: str = "Verify with provider"
    note: str = "Verify availability, credentials, and appointment details directly."
    is_prototype: bool = True


def find_care(specialty: str = "", location: str = "", visit_type: str = "", cost: str = "") -> list[dict[str, str]]:
    providers = [
        CareProvider("provider-1", "MEDORA Community Clinic", "primary care", "local"),
        CareProvider("provider-2", "MEDORA Specialist Network", "specialist", "local"),
    ]
    return [asdict(item) for item in providers if (not specialty or specialty.casefold() in item.specialty.casefold())
            and (not location or location.casefold() in item.location.casefold())
            and (not visit_type or visit_type.casefold() in item.visit_type.casefold())
            and (not cost or cost.casefold() in item.cost.casefold())]