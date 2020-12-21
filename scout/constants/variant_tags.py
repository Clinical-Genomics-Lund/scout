CONSEQUENCE = (
    "deleterious",
    "deleterious_low_confidence",
    "probably_damaging",
    "possibly_damaging",
    "tolerated",
    "tolerated_low_confidence",
    "benign",
    "unknown",
)

CONSERVATION = {
    "gerp": {"conserved_min": 2, "conserved_max": 10},
    "phast": {"conserved_min": 0.8, "conserved_max": 100},
    "phylop": {"conserved_min": 2.5, "conserved_max": 100},
}

FEATURE_TYPES = (
    "exonic",
    "splicing",
    "ncRNA_exonic",
    "intronic",
    "ncRNA",
    "upstream",
    "5UTR",
    "3UTR",
    "downstream",
    "TFBS",
    "regulatory_region",
    "genomic_feature",
    "intergenic_variant",
)

SV_TYPES = ("ins", "del", "dup", "cnv", "inv", "bnd")

GENETIC_MODELS = (
    ("AR_hom", "Autosomal Recessive Homozygote"),
    ("AR_hom_dn", "Autosomal Recessive Homozygote De Novo"),
    ("AR_comp", "Autosomal Recessive Compound"),
    ("AR_comp_dn", "Autosomal Recessive Compound De Novo"),
    ("AD", "Autosomal Dominant"),
    ("AD_dn", "Autosomal Dominant De Novo"),
    ("XR", "X Linked Recessive"),
    ("XR_dn", "X Linked Recessive De Novo"),
    ("XD", "X Linked Dominant"),
    ("XD_dn", "X Linked Dominant De Novo"),
)


VARIANT_CALL = ("Pass", "Filtered", "Not Found", "Not Used")

# Describe conversion between numerical SPIDEX values and human readable.
# Abs is not tractable in mongo query.
SPIDEX_HUMAN = {
    "low": {"neg": [-1, 0], "pos": [0, 1]},
    "medium": {"neg": [-2, -1], "pos": [1, 2]},
    "high": {"neg": [-2, -float("inf")], "pos": [2, float("inf")]},
}

SPIDEX_LEVELS = ("not_reported", "low", "medium", "high")

CANCER_TIER_OPTIONS = {
    "1A": {
        "label": "Tier IA",
        "description": "Strong Clinical Significance. Biomarkers in FDA or guidlines that "
        "predict response, resistance to therapy, diagnosis or prognosis "
        "to specific tumor type.",
        "label_class": "danger",
    },
    "1B": {
        "label": "Tier IB",
        "description": "Potential Clinical Significance Biomarkers in well-powered, concenus "
        "affirmed studies that predict response, resistance to therapy, "
        "diagnostic or prognostic significance to specific tumor type.",
        "label_class": "danger",
    },
    "2C": {
        "label": "Tier IIC",
        "description": "Biomarkers in FDA or guidlines that "
        "predict response, resistance to therapy,"
        "to a different tumor type; are diagnostic or prognostic for "
        "multiple small studies; or serve as study inclusion criteria.",
        "label_class": "warning",
    },
    "2D": {
        "label": "Tier IID",
        "description": "Biomarkers that show plausible therapeutic significance based on "
        "preclinical studies, may assist diagnosis or prognosis based on "
        "small reports.",
        "label_class": "warning",
    },
    "3": {
        "label": "Tier III",
        "description": "Variant of Unknown Clinical Significance-"
        "Not observed in the population, nor in tumor databases."
        "No convincing published evidence of cancer association.",
        "label_class": "primary",
    },
    "4": {
        "label": "Tier IV",
        "description": "Observed at high frequency in the population. No published evidence.",
        "label_class": "default",
    },
}

MANUAL_RANK_OPTIONS = {
    #    8: {
    #        "label": "KP",
    #        "name": "Known pathogenic",
    #        "description": "Known pathogenic, previously known pathogenic in ClinVar, HGMD, literature, etc",
    #        "label_class": "danger",
    #    },
    7: {
        "label": "P",
        "name": "Pathogenic",
        "description": (
            "Pathogenic, novel mutation but overlapping phenotype with known pathogenic, "
            "no further experimental validation needed"
        ),
        "label_class": "danger",
    },
    #    6: {
    #        "label": "NVP",
    #        "name": "Novel validated pathogenic",
    #        "description": "Novel validated pathogenic, novel mutation and validated experimentally",
    #        "label_class": "danger",
    #    },
    #    5: {
    #        "label": "PPP",
    #        "name": "Pathogenic partial phenotype",
    #        "description": (
    #            "Pathogenic partial phenotype, pathogenic variant explains part of patients phenotype, but "
    #            "not all symptoms"
    #        ),
    #        "label_class": "danger",
    #    },
    4: {
        "label": "LP",
        "name": "Likely pathogenic",
        "description": "Likely pathogenic, experimental validation required to prove causality",
        "label_class": "warning",
    },
    3: {
        "label": "Variant of unknown significance",
        "name": "Variant of unknown significance",
        "description": "Uncertain significance",
        "label_class": "primary",
    },
    2: {
        "label": "LB",
        "name": "Likely benign",
        "description": "Likely benign, uncertain significance, but can discard",
        "label_class": "info",
    },
    1: {
        "label": "B",
        "name": "Benign",
        "description": "Benign, does not cause phenotype",
        "label_class": "success",
    },
    # 0: {
    #    "label": "O",
    #    "name": "Other",
    #    "description": "Other, phenotype not related to disease",
    #    "label_class": "default",
    # },
}

DISMISS_VARIANT_OPTIONS = {
    2: {"label": "(F) B/LB ClinVar", "description": "(F) B/LB ClinVar", "evidence": ["clinvar"]},
    3: {"label": "(F) Common gnomAD", "description": "(F) Common gnomAD", "evidence": ["freq"]},
    5: {"label": "(F) Non coding", "description": "(F) Non coding", "evidence": ["transcript"]},
    7: {
        "label": "(F) Probable artefact",
        "description": "(F) Probable artefact",
        "evidence": ["freq", "GT", "inheritance_model"],
    },
    11: {"label": "(F) Not in proband", "description": "(F) Not in proband", "evidence": ["GT"]},
    13: {"label": "B/LB ClinVar", "description": "B/LB ClinVar", "evidence": ["clinvar"]},
    17: {"label": "Common gnomAD", "description": "Common gnomAD", "evidence": ["freq"]},
    19: {
        "label": "No plausible compound",
        "description": "No plausible compound",
        "evidence": ["inheritance_model"],
    },
    23: {
        "label": "Not annotated in OMIM",
        "description": "Not annotated in OMIM",
        "evidence": ["OMIM"],
    },
    29: {"label": "Predicted benign", "description": "Predicted benign", "evidence": ["CADD"]},
    31: {
        "label": "Inherited, unaffected parent",
        "description": "Inherited, unaffected parent",
        "evidence": ["inheritance_model"],
    },
    37: {
        "label": "Irrelevant phenotype",
        "description": "Irrelevant phenotype",
        "evidence": ["OMIM"],
    },
    41: {
        "label": "PubMed, no relevant info",
        "description": "PubMed, no relevant info",
        "evidence": ["type"],
    },
    43: {
        "label": "Technical issues",
        "description": "Technical issues",
        "evidence": ["pileup", "GT"],
    },
}

CANCER_SPECIFIC_VARIANT_DISMISS_OPTIONS = {
    44: {
        "label": "Possible Germline",
        "description": "Variant is possibly a germline event.",
        "evidence": [],
    },
    45: {
        "label": "Low count normal",
        "description": 'Variant has too few reads in normal sample "AD".',
        "evidence": [],
    },
    46: {
        "label": "Low count tumor",
        "description": 'Variant has too few reads in tumor sample. "AD".',
        "evidence": [],
    },
}

MOSAICISM_OPTIONS = {
    1: {
        "label": "Suspected in parent",
        "description": "Variant is suspected to be mosaic in a parent sample.",
        "evidence": ["allele_count"],
    },
    2: {
        "label": "Suspected in affected",
        "description": "Variant is suspected to be mosaic in a affected sample.",
        "evidence": ["allele_count"],
    },
    3: {
        "label": "Confirmed in parent",
        "description": "Variant is confirmed to be mosaic in a parent sample.",
        "evidence": ["allele_count"],
    },
    4: {
        "label": "Confirmed in affected",
        "description": "Variant is confirmed to be mosaic in a affected sample.",
        "evidence": ["allele_count"],
    },
    5: {
        "label": "Not evident in parental reads",
        "description": "Variant was inspected for mosaicism, but not seen in reads from parental samples.",
        "evidence": ["allele_count"],
    },
}
