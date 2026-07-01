import collections

# Knowledge base for diseases and their required symptoms.
# Each disease has a list of symptoms and a minimum number of symptoms
# required to make a confident diagnosis.
KNOWLEDGE_BASE = {
    "Common Cold": {
        "symptoms": ["runny nose", "sore throat", "cough", "fatigue"],
        "min_evidence": 3 # At least 3 symptoms for a confident diagnosis
    },
    "Flu": {
        "symptoms": ["fever", "body aches", "fatigue", "cough", "sore throat"],
        "min_evidence": 4 # At least 4 symptoms for a confident diagnosis
    },
    "Allergies": {
        "symptoms": ["sneezing", "itchy eyes", "runny nose"],
        "min_evidence": 2 # At least 2 symptoms for a confident diagnosis
    },
    "Migraine": {
        "symptoms": ["severe headache", "nausea", "light sensitivity"],
        "min_evidence": 2 # At least 2 symptoms for a confident diagnosis
    }
}

def diagnose_agent(reported_symptoms: list[str]) -> None:
    """
    Simulates an AI agent that makes evidence-based decisions for diagnosis.
    It avoids making assumptions when evidence is insufficient and explicitly
    states when more information is needed.
    """
    print(f"-- Diagnosing based on symptoms: {', '.join(reported_symptoms) if reported_symptoms else 'None'} --")

    confident_diagnoses = []
    potential_diagnoses_needing_more_evidence = collections.defaultdict(list)

    for disease_name, disease_info in KNOWLEDGE_BASE.items():
        required_symptoms = set(disease_info["symptoms"])
        min_evidence = disease_info["min_evidence"]

        # Count how many reported symptoms match the required symptoms for this disease
        matched_symptoms = set(reported_symptoms).intersection(required_symptoms)
        num_matched = len(matched_symptoms)

        # --- Core concept: Evidence-based decision making vs. assumptions ---
        if num_matched >= min_evidence:
            # Sufficient evidence: The agent makes a confident diagnosis.
            confident_diagnoses.append(disease_name)
        elif num_matched > 0:
            # Some evidence, but not enough for a confident diagnosis.
            # The agent recognizes information deficiency and requests more evidence.
            missing_symptoms = required_symptoms - set(reported_symptoms)
            potential_diagnoses_needing_more_evidence[disease_name].extend(list(missing_symptoms))
        # else:
            # No matching symptoms at all for this disease. The agent does not make an assumption.

    if confident_diagnoses:
        print("\n[CONFIDENT DIAGNOSIS]")
        for diagnosis in confident_diagnoses:
            print(f"- Likely: {diagnosis}")
        print("Based on sufficient evidence.")
    elif potential_diagnoses_needing_more_evidence:
        print("\n[INSUFFICIENT EVIDENCE - NEEDS MORE INFORMATION]")
        print("Cannot make a confident diagnosis with current information.")
        print("Consider checking for the following additional symptoms:")
        for disease, missing_symptoms in potential_diagnoses_needing_more_evidence.items():
            print(f"- For potential {disease}: {', '.join(missing_symptoms)}")
        print("The agent explicitly recognizes information deficiency instead of making an assumption.")
    else:
        # No evidence for any known disease
        print("\n[CANNOT DIAGNOSE]")
        print("No known condition matches the reported symptoms, or evidence is too sparse.")
        print("The agent refrains from making any diagnosis due to lack of relevant evidence.")
        print("This prevents potentially harmful assumptions.")

# --- Test Cases ---
if __name__ == "__main__":
    # Case 1: Sufficient evidence for a confident diagnosis
    diagnose_agent(["runny nose", "sore throat", "cough", "fatigue"])

    # Case 2: Some evidence, but not enough for a confident diagnosis. Agent asks for more.
    diagnose_agent(["fever", "body aches"])

    # Case 3: Conflicting or partial evidence for multiple conditions
    diagnose_agent(["runny nose", "itchy eyes", "cough"])

    # Case 4: No relevant evidence
    diagnose_agent(["toothache", "dizziness"])

    # Case 5: Empty symptoms list
    diagnose_agent([])

    # Case 6: Sufficient evidence for another diagnosis
    diagnose_agent(["severe headache", "nausea"])
