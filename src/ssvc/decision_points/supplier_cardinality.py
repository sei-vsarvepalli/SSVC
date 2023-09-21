#!/usr/bin/env python
"""
file: supplier_cardinality
author: adh
created_at: 9/21/23 11:20 AM
"""
from ssvc.decision_points.base import SsvcDecisionPoint, SsvcValue

SUPPLIER_CARDINALITY_1 = SsvcDecisionPoint(
    name="Supplier Cardinality",
    description="How many suppliers are responsible for the vulnerable component and its remediation or mitigation plan?",
    key="SC",
    version="1.0.0",
    values=[
        # One, Multiple
        SsvcValue(
            name="One",
            key="O",
            description="There is only one supplier of the vulnerable component.",
        ),
        SsvcValue(
            name="Multiple",
            key="M",
            description="There are multiple suppliers of the vulnerable component.",
        ),
    ],
)


def main():
    print(SUPPLIER_CARDINALITY_1.to_json(indent=2))


if __name__ == "__main__":
    main()
