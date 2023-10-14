## Executive Summary
On 24th of Aug, 2023 at exactly 2:45 P.M (WAT) one of our websites (www.onlinestore.com) experienced a critical malfunction that resulted in significant downtime and disruption for our users as 80% of users could not process their payment for items already in their cart due to payment API malfunction. The malfunction ended at 3:10 P.M (WAT). This postmortem report aims to provide a detailed analysis of the incident, its causes, and recommendations for preventing future occurrences.
## Timeline of Events
- [24/08/2023, 2:45 P.M (WAT)] - Initial reports of website errors.
- [24/08/2023, 2:48 P.M (WAT)] - a customer complained that she is unable to pay for some items online on the ecommerce store and many users complained of website errors
- [24/08/2023, 2:53 P.M (WAT)] - Database server capacity increased to handle higher loads and temporary workarounds implemented to route traffic away from the affected third-party service.
- [24/08/2023, 2:55 P.M (WAT)] - Database server capacity increased to handle higher loads
- [24/08/2023, 2:48 P.M (WAT)] - the incident was escalated to the engineering team w
- [24/08/2023, 3:10 P.M (WAT)] - Website stability restored.
## Root Cause Analysis
### Our clients website malfunction was primarily caused by a combination of factors, including:
- Database Overload: A sudden surge in traffic overloaded the database server causing a bottleneck.
- Third-Party Api Failure: payment API from a third-party payment provider experienced downtime. 
- Corrective and preventative measures
- Database Optimization: we implemented long-term database optimization strategies to handle traffic spikes more effectively.
- Third-Party Service Redundancy: we created an alternative third-party payment API by initiating a USSD payment option  to mitigate dependencies.
- Monitoring and Alerting: we also enhanced our monitoring systems to proactively identify issues and trigger alerts.

