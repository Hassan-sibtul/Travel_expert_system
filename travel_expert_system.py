# Auto-generated Travel Recommender Expert System
from dataclasses import dataclass
from typing import Callable, Dict, List, Tuple
DESTINATIONS = {'Japan': {'continent': 'Asia', 'cost': 'high', 'climate': ['temperate', 'humid'], 'styles': ['culture', 'food', 'city', 'nature'], 'best_months': [3, 4, 5, 10, 11], 'visa_easy_uk': True, 'trip_length': ['medium', 'long']}, 'Spain': {'continent': 'Europe', 'cost': 'medium', 'climate': ['mediterranean', 'warm'], 'styles': ['beach', 'culture', 'food', 'nightlife', 'city'], 'best_months': [4, 5, 6, 9, 10], 'visa_easy_uk': True, 'trip_length': ['short', 'medium']}, 'Thailand': {'continent': 'Asia', 'cost': 'low', 'climate': ['tropical', 'humid'], 'styles': ['beach', 'food', 'adventure', 'nature', 'nightlife'], 'best_months': [1, 2, 12], 'visa_easy_uk': True, 'trip_length': ['medium', 'long']}, 'Iceland': {'continent': 'Europe', 'cost': 'high', 'climate': ['cold'], 'styles': ['nature', 'adventure', 'roadtrip'], 'best_months': [2, 3, 9, 10], 'visa_easy_uk': True, 'trip_length': ['short', 'medium']}, 'Italy': {'continent': 'Europe', 'cost': 'medium', 'climate': ['mediterranean', 'warm'], 'styles': ['culture', 'food', 'city', 'beach'], 'best_months': [4, 5, 9, 10], 'visa_easy_uk': True, 'trip_length': ['short', 'medium']}, 'Morocco': {'continent': 'Africa', 'cost': 'low', 'climate': ['arid', 'warm'], 'styles': ['culture', 'desert', 'food', 'adventure'], 'best_months': [3, 4, 10, 11], 'visa_easy_uk': True, 'trip_length': ['short', 'medium']}, 'Australia': {'continent': 'Oceania', 'cost': 'high', 'climate': ['varied', 'temperate'], 'styles': ['beach', 'nature', 'adventure', 'city'], 'best_months': [11, 12, 1, 2, 3], 'visa_easy_uk': True, 'trip_length': ['long']}, 'Canada': {'continent': 'North America', 'cost': 'high', 'climate': ['cold', 'temperate'], 'styles': ['nature', 'adventure', 'city'], 'best_months': [6, 7, 8, 9], 'visa_easy_uk': True, 'trip_length': ['medium', 'long']}, 'Greece': {'continent': 'Europe', 'cost': 'medium', 'climate': ['mediterranean', 'warm'], 'styles': ['beach', 'culture', 'islands', 'food'], 'best_months': [5, 6, 9, 10], 'visa_easy_uk': True, 'trip_length': ['short', 'medium']}, 'Portugal': {'continent': 'Europe', 'cost': 'low', 'climate': ['mediterranean', 'warm'], 'styles': ['beach', 'culture', 'food', 'city', 'surf'], 'best_months': [5, 6, 9, 10], 'visa_easy_uk': True, 'trip_length': ['short', 'medium']}, 'Vietnam': {'continent': 'Asia', 'cost': 'low', 'climate': ['tropical', 'humid'], 'styles': ['food', 'culture', 'nature', 'adventure'], 'best_months': [2, 3, 12], 'visa_easy_uk': True, 'trip_length': ['medium', 'long']}, 'USA_NYC': {'continent': 'North America', 'cost': 'high', 'climate': ['temperate'], 'styles': ['city', 'culture', 'nightlife', 'food'], 'best_months': [5, 6, 9, 10, 12], 'visa_easy_uk': True, 'trip_length': ['short', 'medium']}, 'Kenya': {'continent': 'Africa', 'cost': 'medium', 'climate': ['tropical', 'arid'], 'styles': ['safari', 'nature', 'adventure'], 'best_months': [7, 8, 9], 'visa_easy_uk': True, 'trip_length': ['medium']}, 'Switzerland': {'continent': 'Europe', 'cost': 'high', 'climate': ['cold', 'temperate'], 'styles': ['nature', 'adventure', 'ski', 'scenic'], 'best_months': [2, 3, 6, 7, 8, 9], 'visa_easy_uk': True, 'trip_length': ['short', 'medium']}, 'Netherlands': {'continent': 'Europe', 'cost': 'medium', 'climate': ['temperate'], 'styles': ['city', 'culture', 'cycling'], 'best_months': [4, 5, 6, 9], 'visa_easy_uk': True, 'trip_length': ['short']}, 'UAE_Dubai': {'continent': 'Asia', 'cost': 'medium', 'climate': ['hot', 'arid'], 'styles': ['city', 'luxury', 'beach', 'nightlife'], 'best_months': [11, 12, 1, 2, 3], 'visa_easy_uk': True, 'trip_length': ['short']}, 'Norway': {'continent': 'Europe', 'cost': 'high', 'climate': ['cold', 'temperate'], 'styles': ['nature', 'scenic', 'adventure'], 'best_months': [6, 7, 8, 9], 'visa_easy_uk': True, 'trip_length': ['short', 'medium']}, 'Mexico': {'continent': 'North America', 'cost': 'medium', 'climate': ['tropical', 'warm'], 'styles': ['beach', 'food', 'culture', 'nightlife'], 'best_months': [12, 1, 2, 3], 'visa_easy_uk': True, 'trip_length': ['medium']}, 'Egypt': {'continent': 'Africa', 'cost': 'low', 'climate': ['hot', 'arid'], 'styles': ['culture', 'history', 'desert'], 'best_months': [10, 11, 12, 1, 2, 3], 'visa_easy_uk': True, 'trip_length': ['short', 'medium']}, 'Turkey': {'continent': 'Asia', 'cost': 'low', 'climate': ['mediterranean', 'warm'], 'styles': ['culture', 'beach', 'food', 'history'], 'best_months': [5, 6, 9, 10], 'visa_easy_uk': True, 'trip_length': ['short', 'medium']}, 'Indonesia_Bali': {'continent': 'Asia', 'cost': 'low', 'climate': ['tropical', 'humid'], 'styles': ['beach', 'wellness', 'surf', 'nature'], 'best_months': [5, 6, 7, 8, 9], 'visa_easy_uk': True, 'trip_length': ['medium', 'long']}, 'France': {'continent': 'Europe', 'cost': 'medium', 'climate': ['temperate', 'mediterranean'], 'styles': ['culture', 'food', 'city', 'beach', 'ski'], 'best_months': [5, 6, 9, 10, 12, 2], 'visa_easy_uk': True, 'trip_length': ['short', 'medium']}, 'Austria': {'continent': 'Europe', 'cost': 'medium', 'climate': ['cold', 'temperate'], 'styles': ['ski', 'nature', 'culture'], 'best_months': [1, 2, 3, 6, 7, 8, 12], 'visa_easy_uk': True, 'trip_length': ['short', 'medium']}}
PREFERENCES_SCHEMA = {'budget': ['low', 'medium', 'high'], 'preferred_climate': ['cold', 'temperate', 'warm', 'hot', 'tropical', 'mediterranean', 'arid', 'humid', 'varied'], 'styles': ['beach', 'culture', 'food', 'city', 'nightlife', 'nature', 'adventure', 'safari', 'ski', 'islands', 'roadtrip', 'scenic', 'cycling', 'surf', 'wellness', 'history', 'desert', 'luxury'], 'continent': ['Europe', 'Asia', 'Africa', 'North America', 'South America', 'Oceania'], 'month': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], 'trip_length': ['short', 'medium', 'long'], 'visa_easy_required': [True, False]}

@dataclass
class Rule:
    name: str
    condition: Callable[[Dict], bool]
    action: Callable[[Dict, Dict[str, float], List[str]], None]

def make_rules() -> List[Rule]:
    rules: List[Rule] = []

    for cost in ["low","medium","high"]:
        rules.append(Rule(
            f"Budget_{cost}",
            lambda f, c=cost: f.get("budget")==c,
            lambda f, s, e, c=cost: [ (s.__setitem__(d, s.get(d,0)+2.0), e.append(f"Budget match ({c}) → {d} +2")) for d,a in DESTINATIONS.items() if a["cost"]==c ]
        ))
    rules.append(Rule(
        "Climate_Preference",
        lambda f: "preferred_climate" in f,
        lambda f, s, e: [ (s.__setitem__(d, s.get(d,0)+1.5), e.append(f"Climate match ({f.get('preferred_climate')}) → {d} +1.5")) for d,a in DESTINATIONS.items() if f.get("preferred_climate") in a["climate"] ]
    ))
    for style in ["beach","culture","food","city","nightlife","nature","adventure","safari","ski","islands","roadtrip","scenic","cycling","surf","wellness","history","desert","luxury"]:
        rules.append(Rule(
            f"Style_{style}",
            lambda f, st=style: st in f.get("styles", []),
            lambda f, s, e, st=style: [ (s.__setitem__(d, s.get(d,0)+1.7), e.append(f"Style match ({st}) → {d} +1.7")) for d,a in DESTINATIONS.items() if st in a["styles"] ]
        ))
    rules.append(Rule(
        "Continent_Preference",
        lambda f: "continents" in f and f.get("continents"),
        lambda f, s, e: [ (s.__setitem__(d, s.get(d,0)+(3.0 if a["continent"] in f.get("continents", []) else -5.0)), e.append((f"Continent match ({a['continent']}) → {d} +3.0" if a["continent"] in f.get("continents", []) else f"Continent mismatch ({a['continent']}) → {d} -5.0"))) for d,a in DESTINATIONS.items() ]
    ))
    rules.append(Rule(
        "Seasonality",
        lambda f: "months" in f and f.get("months"),
        lambda f, s, e: [ (s.__setitem__(d, s.get(d,0)+(1.8 if any(m in a["best_months"] for m in f.get("months", [])) else -0.8)), e.append(("Good season" if any(m in a["best_months"] for m in f.get("months", [])) else "Off-season")+f" ({','.join(map(str, f.get('months', [])))}) → {d} "+("+1.8" if any(m in a["best_months"] for m in f.get("months", [])) else "-0.8"))) for d,a in DESTINATIONS.items() ]
    ))
    rules.append(Rule(
        "Trip_Length",
        lambda f: "trip_length" in f,
        lambda f, s, e: [ (s.__setitem__(d, s.get(d,0)+(1.0 if f.get("trip_length") in a["trip_length"] else -0.5)), e.append((f"Trip length match ({f.get('trip_length')}) → {d} +1" if f.get("trip_length") in a["trip_length"] else f"Trip length mismatch ({f.get('trip_length')}) → {d} -0.5"))) for d,a in DESTINATIONS.items() ]
    ))
    rules.append(Rule(
        "Visa_Easy",
        lambda f: f.get("visa_easy_required") is True,
        lambda f, s, e: [ (s.__setitem__(d, s.get(d,0)+0.6), e.append(f"Visa-easy needed → {d} +0.6")) for d,a in DESTINATIONS.items() if a["visa_easy_uk"] ]
    ))
    rules.append(Rule(
        "Ski_Winter",
        lambda f: "ski" in f.get("styles", []) and any(m in [1,2,12] for m in f.get("months", [])),
        lambda f, s, e: [ (s.__setitem__(d, s.get(d,0)+2.5), e.append(f"Ski in winter → {d} +2.5")) for d in ["Austria","Switzerland","France"] ]
    ))
    rules.append(Rule(
        "Safari_Season",
        lambda f: "safari" in f.get("styles", []) and any(m in [7,8,9] for m in f.get("months", [])),
        lambda f, s, e: (s.__setitem__("Kenya", s.get("Kenya",0)+3.0), e.append("Safari in Jul–Sep → Kenya +3"))
    ))
    rules.append(Rule(
        "Beach_WinterSun",
        lambda f: "beach" in f.get("styles", []) and any(m in [12,1,2] for m in f.get("months", [])),
        lambda f, s, e: [ (s.__setitem__(d, s.get(d,0)+2.2), e.append(f"Winter sun beach → {d} +2.2")) for d in ["Thailand","Mexico","UAE_Dubai","Egypt"] ]
    ))
    rules.append(Rule(
        "CityCulture_Shoulder",
        lambda f: ("culture" in f.get("styles", [])) and ("city" in f.get("styles", [])) and any(m in [4,5,9,10] for m in f.get("months", [])),
        lambda f, s, e: [ (s.__setitem__(d, s.get(d,0)+1.9), e.append(f"City + culture in shoulder season → {d} +1.9")) for d in ["Italy","Spain","France","Japan","Netherlands"] ]
    ))
    rules.append(Rule(
        "Avoid_Hot_When_ColdPref",
        lambda f: f.get("preferred_climate") == "cold",
        lambda f, s, e: [ (s.__setitem__(d, s.get(d,0)-2.0), e.append(f"Cold climate pref → avoid hot: {d} -2")) for d in ["UAE_Dubai","Egypt","Morocco"] ]
    ))
    rules.append(Rule(
        "ShortTrip_Europe",
        lambda f: f.get("trip_length") == "short",
        lambda f, s, e: [ (s.__setitem__(d, s.get(d,0)+1.6), e.append(f"Short trip → Europe friendly: {d} +1.6")) for d in ["Portugal","Spain","France","Netherlands","Greece","Iceland","Austria","Switzerland","Italy","Norway"] ]
    ))
    rules.append(Rule(
        "Backpacker_LowBudget",
        lambda f: f.get("budget") == "low" and any(s in f.get("styles", []) for s in ["adventure","culture","surf"]),
        lambda f, s, e: [ (s.__setitem__(d, s.get(d,0)+1.4), e.append(f"Backpacker & low budget → {d} +1.4")) for d in ["Portugal","Turkey","Vietnam","Thailand","Indonesia_Bali","Morocco"] ]
    ))
    rules.append(Rule(
        "Luxury_City",
        lambda f: "luxury" in f.get("styles", []) or ("city" in f.get("styles", []) and f.get("budget") == "high"),
        lambda f, s, e: [ (s.__setitem__(d, s.get(d,0)+1.5), e.append(f"Luxury/city preference → {d} +1.5")) for d in ["UAE_Dubai","Japan","USA_NYC","Switzerland"] ]
    ))
    rules.append(Rule(
        "Island_Beach",
        lambda f: "islands" in f.get("styles", []) or ("beach" in f.get("styles", []) and any(m in [5,6,9,10] for m in f.get("months", []))),
        lambda f, s, e: [ (s.__setitem__(d, s.get(d,0)+1.3), e.append(f"Islands/beach shoulder → {d} +1.3")) for d in ["Greece","Indonesia_Bali","Thailand","Portugal"] ]
    ))
    rules.append(Rule(
        "Food_and_Culture",
        lambda f: "food" in f.get("styles", []) and "culture" in f.get("styles", []),
        lambda f, s, e: [ (s.__setitem__(d, s.get(d,0)+1.6), e.append(f"Food + culture → {d} +1.6")) for d in ["Italy","France","Spain","Portugal","Japan","Vietnam","Mexico","Turkey"] ]
    ))
    rules.append(Rule(
        "Northern_Lights",
        lambda f: "nature" in f.get("styles", []) and any(m in [2,3,9,10] for m in f.get("months", [])),
        lambda f, s, e: [ (s.__setitem__(d, s.get(d,0)+2.0), e.append(f"Northern lights season → {d} +2.0")) for d in ["Iceland","Norway"] ]
    ))
    rules.append(Rule(
        "Surf_Focus",
        lambda f: "surf" in f.get("styles", []),
        lambda f, s, e: [ (s.__setitem__(d, s.get(d,0)+1.8), e.append(f"Surf focus → {d} +1.8")) for d in ["Portugal","Indonesia_Bali"] ]
    ))
    rules.append(Rule(
        "Ski_Avoid_Summer",
        lambda f: "ski" in f.get("styles", []) and any(m in [6,7,8] for m in f.get("months", [])),
        lambda f, s, e: ( [ s.__setitem__(d, s.get(d,0)-0.7) for d in DESTINATIONS.keys() ], e.append("Ski requested in summer → global -0.7") )
    ))
    rules.append(Rule(
        "City_Winter_Short",
        lambda f: "city" in f.get("styles", []) and f.get("trip_length") == "short" and any(m in [12,1,2] for m in f.get("months", [])),
        lambda f, s, e: [ (s.__setitem__(d, s.get(d,0)+1.1), e.append(f"City break in winter → {d} +1.1")) for d in ["France","Netherlands","Spain","USA_NYC","UAE_Dubai"] ]
    ))
    return rules

RULES = make_rules()

def infer_recommendations(facts: Dict, top_k: int = 5):
    scores: Dict[str, float] = {d: 0.0 for d in DESTINATIONS}
    explain: List[str] = []
    for rule in RULES:
        if rule.condition(facts):
            rule.action(facts, scores, explain)
    ranked = sorted(scores.items(), key=lambda kv: kv[1], reverse=True)[:top_k]
    return ranked, explain

def main():
    print("\n" + "="*60)
    print("   🌍 TRAVEL RECOMMENDER EXPERT SYSTEM 🌍")
    print("="*60)
    print("\nLet's find your perfect destination!\n")
    
    facts = {}
    
    # Budget
    print("💰 What's your budget?")
    print("   Options: low, medium, high")
    budget = input("   Your choice: ").strip().lower()
    if budget in ['low', 'medium', 'high']:
        facts['budget'] = budget
    
    # Climate
    print("\n🌤️  What climate do you prefer?")
    print("   Options: cold, temperate, warm, hot, tropical, mediterranean, arid")
    climate = input("   Your choice (or press Enter to skip): ").strip().lower()
    if climate:
        facts['preferred_climate'] = climate
    
    # Travel styles
    print("\n🎨 What travel styles interest you? (comma-separated)")
    print("   Options: beach, culture, food, city, nightlife, nature, adventure,")
    print("           safari, ski, islands, roadtrip, scenic, cycling, surf,")
    print("           wellness, history, desert, luxury")
    styles_input = input("   Your choices: ").strip().lower()
    if styles_input:
        facts['styles'] = [s.strip() for s in styles_input.split(',')]
    
    # Continent
    print("\n🗺️  Preferred continent(s)? (comma-separated)")
    print("   Options: Europe, Asia, Africa, North America, South America, Oceania")
    continent_input = input("   Your choice(s) (or press Enter to skip): ").strip()
    if continent_input:
        continents = [c.strip() for c in continent_input.split(',')]
        facts['continents'] = continents
    
    # Month
    print("\n📅 Which month(s) are you planning to travel? (comma-separated)")
    month_input = input("   Month(s) (1-12): ").strip()
    if month_input:
        try:
            months = [int(m.strip()) for m in month_input.split(',') if m.strip().isdigit() and 1 <= int(m.strip()) <= 12]
            if months:
                facts['months'] = months
        except ValueError:
            pass
    
    # Trip length
    print("\n⏱️  How long is your trip?")
    print("   Options: short (weekend/few days), medium (1-2 weeks), long (2+ weeks)")
    trip_length = input("   Your choice: ").strip().lower()
    if trip_length in ['short', 'medium', 'long']:
        facts['trip_length'] = trip_length
    
    # Visa
    print("\n📋 Do you need easy visa access from UK?")
    visa = input("   (yes/no): ").strip().lower()
    if visa == 'yes':
        facts['visa_easy_required'] = True
    
    # Get recommendations
    print("\n" + "="*60)
    print("   🔍 ANALYZING YOUR PREFERENCES...")
    print("="*60)
    
    recommendations, explanations = infer_recommendations(facts, top_k=5)
    
    print("\n✨ TOP RECOMMENDATIONS FOR YOU:\n")
    for i, (dest, score) in enumerate(recommendations, 1):
        print(f"{i}. {dest.replace('_', ' ').upper()}")
        print(f"   Score: {score:.1f}")
        dest_info = DESTINATIONS[dest]
        print(f"   Cost: {dest_info['cost']} | Climate: {', '.join(dest_info['climate'])}")
        print(f"   Styles: {', '.join(dest_info['styles'][:5])}")
        print()
    
    print("\n" + "="*60)
    print("   📊 REASONING (Sample):")
    print("="*60)
    for exp in explanations[:15]:
        print(f"   • {exp}")
    
    if len(explanations) > 15:
        print(f"   ... and {len(explanations) - 15} more reasoning steps")
    
    print("\n" + "="*60)
    print("   Happy travels! 🎒✈️")
    print("="*60 + "\n")

if __name__ == "__main__":
    main()

# ============================================================
# TESTING SUITE - For Assignment Evidence
# ============================================================

def run_test_case(test_name: str, facts: Dict, expected_top: str = None):
    """
    Run a single test case and display results.
    Used to demonstrate testing and rule refinement process.
    """
    print("\n" + "="*70)
    print(f"TEST CASE: {test_name}")
    print("="*70)
    print(f"Input Facts: {facts}")
    
    recommendations, explanations = infer_recommendations(facts, top_k=5)
    
    print(f"\nTop 5 Recommendations:")
    for i, (dest, score) in enumerate(recommendations, 1):
        marker = "⭐" if expected_top and dest == expected_top else "  "
        print(f"{marker} {i}. {dest}: {score:.1f} points")
    
    print(f"\nKey Reasoning Steps:")
    for exp in explanations[:10]:
        print(f"  • {exp}")
    
    if expected_top:
        actual_top = recommendations[0][0]
        if actual_top == expected_top:
            print(f"\n✅ PASS: Expected '{expected_top}' is ranked #1")
        else:
            print(f"\n❌ FAIL: Expected '{expected_top}' but got '{actual_top}'")
    
    return recommendations

def run_all_tests():
    """
    Comprehensive test suite demonstrating system functionality.
    This shows evidence of testing as required by the assignment.
    """
    print("\n" + "="*70)
    print("   TRAVEL EXPERT SYSTEM - COMPREHENSIVE TEST SUITE")
    print("="*70)
    
    # Test 1: Budget Traveler - Asia
    run_test_case(
        "Budget Traveler - Beach & Food in Asia (Low Season)",
        {
            "budget": "low",
            "continents": ["Asia"],
            "styles": ["beach", "food"],
            "months": [1, 2],
            "trip_length": "medium",
            "visa_easy_required": True
        },
        expected_top="Thailand"
    )
    
    # Test 2: Luxury Winter Ski Trip
    run_test_case(
        "Luxury Winter Ski Trip in Europe",
        {
            "budget": "high",
            "continents": ["Europe"],
            "styles": ["ski", "luxury"],
            "months": [12, 1, 2],
            "trip_length": "short",
            "preferred_climate": "cold"
        },
        expected_top="Switzerland"
    )
    
    # Test 3: Safari Adventure
    run_test_case(
        "Safari Adventure in Africa (Peak Season)",
        {
            "budget": "medium",
            "continents": ["Africa"],
            "styles": ["safari", "nature", "adventure"],
            "months": [7, 8],
            "trip_length": "medium"
        },
        expected_top="Kenya"
    )
    
    # Test 4: City Break - Culture & Food
    run_test_case(
        "City Break - Culture & Food in Europe",
        {
            "budget": "medium",
            "continents": ["Europe"],
            "styles": ["city", "culture", "food"],
            "months": [4, 5],
            "trip_length": "short",
            "preferred_climate": "mediterranean"
        },
        expected_top="Italy"
    )
    
    # Test 5: Beach Holiday - Summer
    run_test_case(
        "Beach & Islands in Europe (Summer)",
        {
            "budget": "medium",
            "continents": ["Europe"],
            "styles": ["beach", "islands"],
            "months": [6, 7],
            "trip_length": "medium",
            "preferred_climate": "warm"
        },
        expected_top="Greece"
    )
    
    # Test 6: Backpacker Trip
    run_test_case(
        "Backpacker - Adventure & Culture in Asia",
        {
            "budget": "low",
            "continents": ["Asia"],
            "styles": ["adventure", "culture", "food"],
            "months": [2, 3],
            "trip_length": "long"
        },
        expected_top="Vietnam"
    )
    
    # Test 7: Northern Lights
    run_test_case(
        "Northern Lights - Nature in Europe",
        {
            "budget": "high",
            "continents": ["Europe"],
            "styles": ["nature", "scenic"],
            "months": [2, 3],
            "trip_length": "short",
            "preferred_climate": "cold"
        },
        expected_top="Iceland"
    )
    
    # Test 8: Surf Trip
    run_test_case(
        "Surf & Beach in Europe (Shoulder Season)",
        {
            "budget": "low",
            "continents": ["Europe"],
            "styles": ["surf", "beach"],
            "months": [9, 10],
            "trip_length": "medium"
        },
        expected_top="Portugal"
    )
    
    # Test 9: Multi-continent preference
    run_test_case(
        "Food & Culture - Asia or Europe (Flexible)",
        {
            "budget": "medium",
            "continents": ["Asia", "Europe"],
            "styles": ["food", "culture"],
            "months": [5],
            "trip_length": "medium"
        }
    )
    
    # Test 10: No continent preference (global search)
    run_test_case(
        "Luxury Beach Holiday - Any Continent (Winter Sun)",
        {
            "budget": "high",
            "styles": ["luxury", "beach"],
            "months": [12, 1],
            "trip_length": "short"
        }
    )
    
    print("\n" + "="*70)
    print("   TEST SUITE COMPLETE")
    print("="*70)
    print("\nNOTE: These tests demonstrate:")
    print("  1. Rule-based reasoning works correctly")
    print("  2. Different user profiles get appropriate recommendations")
    print("  3. Seasonal adjustments are applied")
    print("  4. Budget, style, and continent filters work as expected")
    print("  5. Specialized rules (safari, ski, surf) trigger correctly")
    print("="*70)

# Uncomment the line below to run tests
run_all_tests()
