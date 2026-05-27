#### **ER Operational Efficiency \& Bottleneck Analysis**







##### Project Overview





&#x20;        Analyzed historical Emergency Room visit data to identify peak patient hours, operational bottlenecks, staffing pressure, and factors affecting patient wait times and satisfaction. The project uses time-based operational analysis to evaluate ER workflow efficiency and support data-driven staffing and resource allocation decisions.







##### Business Problem





* Identify peak ER demand periods
* Detect operational bottlenecks causing delays
* Analyze staffing pressure and workload distribution
* Evaluate the relationship between wait times and patient satisfaction
* Support operational decision-making using data-driven insights







##### Dataset Overview





Rows       : 5,000 simulated patient visits

Columns    : 20 features, including hospital details, patient visit specifics, and outcomes

Timeframe  : One year of simulated data (2024)







Visit ID                     : Unique identifier for each visit.

Patient ID                   : Unique identifier for each patient.

Hospital ID                  : Unique identifier for each hospital.

Hospital Name                : Name of the hospital.

Region                       : Classification as Urban or Rural.

Visit Date                   : Date and time of the patient’s visit.

Day of Week                  : Day of the week (e.g., Monday, Tuesday).

Season                       : Season of the visit (Winter, Spring, Summer, Fall).

Time of Day                  : Time slot of the visit (e.g., Early Morning, Afternoon).

Urgency Level                : Urgency classification: Critical, High, Medium, Low.

Nurse-to-Patient Ratio       : Ratio of nurses to patients during the visit.

Specialist Availability      : Number of specialists available at the hospital.

Facility Size (Beds)         : Number of available beds at the facility.

Time to Registration (min)   : Time taken to complete registration.

Time to Triage (min)         : Time taken for triage assessment.

Time to Medical Professional (min): Time taken to see a doctor or healthcare professional.

Total Wait Time (min)        : Total time from arrival to seeing a medical professional.

Patient Outcome              : Outcome of the visit (Admitted, Discharged, Left Without Being Seen).

Patient Satisfaction         : Satisfaction score (1 to 5, with 5 being the highest).









##### Cleaning Log





Performed data validation and preprocessing in Power Query including data type correction, column standardization, handling missing values, and creation of time-based analytical fields to support operational analysis Like HourLabel, WaittimeCategory, WeekdayLabel.





##### Key Insights





###### **Peak ER demand occurs during specific hourly periods**



&#x20;   -- The dashboard identified consistent spikes in ER visits during high-demand operational hours, with Monday and Tuesday recording the highest overall patient volumes.





###### **Doctor-stage delays are the main operational bottleneck**



&#x20;  -- Average doctor wait times remained significantly higher than other workflow stages, indicating that doctor availability is the primary contributor to extended ER wait times



###### **Longer wait times negatively impact patient satisfaction**



&#x20;  -- Patients categorized under long wait durations reported satisfaction scores as low as 1.8/5, while short wait categories maintained satisfaction levels above 4.6/5







##### Recommendations





###### **Optimize staffing during peak demand periods**



&#x20; -- Increase doctor and triage staff coverage during high-volume hours and weekdays to reduce congestion and improve operational efficiency.



###### **Improve patient flow management**



&#x20;-- Implement fast-track consultation processes for low-urgency patients and monitor workload distribution to reduce doctor-stage bottlenecks.



###### **Reduce wait times to improve patient experience**



&#x20;-- Introduce queue visibility systems, proactive communication, and operational monitoring to minimize delays and maintain higher patient satisfaction levels.







##### Tools \& Technologies





* Microsoft Excel
* Power Query
* Pivot Tables
* Pivot Charts
* Conditional Formatting Heatmaps
* Interactive Slicers



