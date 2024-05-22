partial_matches = [
    "All Nippon Airways -> ANA All Nippon Airways",
    "Jetstar -> Jetstar Airways",
    "Indonesia AirAsia -> AirAsia",
    "Scoot Tigerair -> Scoot",
    "Thai AirAsia X -> AirAsia",
    "Eva Air -> EVA Air",
    "LATAM Airlines -> LATAM",
    "Virgin Atlantic Airways -> Virgin Atlantic",
    "Citilink Indonesia -> Citilink",
    "Thai Airways International -> Thai Airways",
    "V Australia -> Virgin Australia",
    "Indonesia AirAsia Extra -> AirAsia",
    "AirAsia X -> AirAsia",
]

mapping = {}

for match in partial_matches:
    before, after = match.split(" -> ")
    mapping[before.strip()] = after.strip()

print(mapping)

mapping = {
    "All Nippon Airways": "ANA All Nippon Airways",
    "Jetstar": "Jetstar Airways",
    "Indonesia AirAsia": "AirAsia",
    "Scoot Tigerair": "Scoot",
    "Thai AirAsia X": "AirAsia",
    "Eva Air": "EVA Air",
    "LATAM Airlines": "LATAM",
    "Virgin Atlantic Airways": "Virgin Atlantic",
    "Citilink Indonesia": "Citilink",
    "Thai Airways International": "Thai Airways",
    "V Australia": "Virgin Australia",
    "Indonesia AirAsia Extra": "AirAsia",
    "AirAsia X": "AirAsia",
}
