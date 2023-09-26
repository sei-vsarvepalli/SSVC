The Accessible Attack Surface of the Affected System or Service

| Value | Key | Description |
| --- | --- | --- |
| Small | S | Local service or program; highly controlled network |
| Controlled | C | Networked service with some access restrictions or mitigations already in place (whether locally or on the network). A successful mitigation must reliably interrupt the adversary’s attack, which requires the attack is detectable both reliably and quickly enough to respond. Controlled covers the situation in which a vulnerability can be exploited through chaining it with other vulnerabilities. The assumption is that the number of steps in the attack path is relatively low; if the path is long enough that it is implausible for an adversary to reliably execute it, then exposure should be small. |
| Open | O | Internet or another widely accessible network where access cannot plausibly be restricted or controlled (e.g., DNS servers, web servers, VOIP servers, email servers) |