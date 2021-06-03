# covid-vaccine-tracker

### Purpose
1. Given state and city, return the list of all vaccine centres available
2. Optionally pass parameters like, dose (first or second), price, etc
3. Polling for vaccine availability
4. Notify user (message/email) about (vaccine_type, doses_available, center_name)
5. Show the number of vaccine doses available in any city on given date. Plot a graph on vaccine availabilities or amount. 

#### Search by district
https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin?pincode=221001&date=01-06-2021


https://cdn-api.co-vin.in/api/v2/admin/location/districts/34

#### Session object
```
[{'session_id': 'cd8d93bd-a7d8-438b-bdab-2e164f46370a',
'date': '01-06-2021',
'available_capacity': 0,
'min_age_limit': 45,
'vaccine': 'COVISHIELD',
'slots': ['10:00AM-11:00AM',
'11:00AM-12:00PM',
'12:00PM-01:00PM',
'01:00PM-04:00PM'],
'available_capacity_dose1': 0,
'available_capacity_dose2': 0}]
```

Parameters to display in sessions table:


### Resources
1. https://apisetu.gov.in/public/api/cowin