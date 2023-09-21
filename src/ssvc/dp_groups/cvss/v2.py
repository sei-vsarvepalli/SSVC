#!/usr/bin/env python
"""
file: v2
author: adh
created_at: 9/20/23 12:54 PM
"""

from ssvc.dp_groups.base import SsvcDecisionPointGroup
from ssvc.decision_points.cvss.access_vector import ACCESS_VECTOR_2
from ssvc.decision_points.cvss.access_complexity import (
    ACCESS_COMPLEXITY_2,
)
from ssvc.decision_points.cvss.authentication import AUTHENTICATION_2
from ssvc.decision_points.cvss.availability_requirement import (
    AVAILABILITY_REQUIREMENT_1,
)
from ssvc.decision_points.cvss.collateral_damage_potential import (
    COLLATERAL_DAMAGE_POTENTIAL_2,
)
from ssvc.decision_points.cvss.confidentiality_impact import (
    CONFIDENTIALITY_IMPACT_1,
)
from ssvc.decision_points.cvss.confidentiality_requirement import (
    CONFIDENTIALITY_REQUIREMENT_1,
)
from ssvc.decision_points.cvss.exploitability import (
    EXPLOITABILITY_1_1,
)
from ssvc.decision_points.cvss.integrity_impact import (
    INTEGRITY_IMPACT_1,
)
from ssvc.decision_points.cvss.availability_impact import (
    AVAILABILITY_IMPACT_1,
)
from ssvc.decision_points.cvss.integrity_requirement import (
    INTEGRITY_REQUIREMENT_1,
)
from ssvc.decision_points.cvss.remediation_level import (
    REMEDIATION_LEVEL_1_1,
)
from ssvc.decision_points.cvss.report_confidence import (
    REPORT_CONFIDENCE_1_1,
)
from ssvc.decision_points.cvss.target_distribution import (
    TARGET_DISTRIBUTION_1_1,
)

CVSSv2 = SsvcDecisionPointGroup(
    name="CVSS Version 2",
    description="The Common Vulnerability Scoring System (CVSS) is a free and open industry standard for assessing the severity of computer system security vulnerabilities. CVSS attempts to assign severity scores to vulnerabilities, allowing responders to prioritize responses and resources according to threat. Scores are calculated based on a formula that depends on several metrics that approximate ease of exploit and the impact of exploit. Scores range from 0 to 10, with 10 being the most severe.",
    key="CVSSv2",
    version="2.0",
    decision_points=[
        ACCESS_VECTOR_2,
        ACCESS_COMPLEXITY_2,
        AUTHENTICATION_2,
        CONFIDENTIALITY_IMPACT_1,
        INTEGRITY_IMPACT_1,
        AVAILABILITY_IMPACT_1,
        EXPLOITABILITY_1_1,
        REMEDIATION_LEVEL_1_1,
        REPORT_CONFIDENCE_1_1,
        COLLATERAL_DAMAGE_POTENTIAL_2,
        TARGET_DISTRIBUTION_1_1,
        CONFIDENTIALITY_REQUIREMENT_1,
        INTEGRITY_REQUIREMENT_1,
        AVAILABILITY_REQUIREMENT_1,
    ],
)


def main():
    print(CVSSv2.to_json(indent=2))


if __name__ == "__main__":
    main()
