PREFIXES = [
    "HKQuantityTypeIdentifier",
    "HKCategoryTypeIdentifier",
    "HKCharacteristicTypeIdentifier",
    "HKWorkoutActivityType",
    "HKDataType",
]


def short_name(identifier: str) -> str:
    for prefix in PREFIXES:
        if identifier.startswith(prefix):
            return identifier.removeprefix(prefix)

    return identifier