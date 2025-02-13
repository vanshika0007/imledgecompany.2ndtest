                                                                          automation readme file
## Overview
This Selenium automation script performs the following tasks on the Kloudship QA environment:
1. Logs into the application.
2. Adds a package with a random dimension.
3. Deletes the added package.
4. Logs out and closes the browser.

## Prerequisites
Ensure you have the following installed before running the script:
- Python 3.x
- Google Chrome browser
- ChromeDriver (Ensure compatibility with your Chrome version)
- Required Python packages:
  ```sh
  pip install selenium
  ```

## Configuration
- **URL**: `https://ecspro-qa.kloudship.com`
- **Credentials**:
  - Username: `kloudship.qa.automation@mailinator.com`
  - Password: `Password1`

## Script Breakdown
### 1. **Login Function**
Logs into the application using the provided credentials.

### 2. **Add Package Function**
- Navigates to the "Package Types" section.
- Adds a package with a random dimension.
- Logs out.

### 3. **Delete Package Function**
- Navigates to the "Package Types" section.
- Finds and deletes the package added previously.
- Logs out.

### 4. **Execution**
- The script first adds a package, retrieves its name, and then deletes the same package.
- Finally, it closes the browser.

## Running the Script
Run the script using the command:
```sh
python script.py
```
Ensure that the `chromedriver` is in your system's PATH or specify its location in the script.

## Notes
- The script uses explicit `time.sleep()` calls for waiting, which can be replaced with WebDriver waits for better performance.
- Modify the package name logic if dynamic naming conventions are required.
- Ensure network connectivity and proper credentials before execution.

                                                                postman readme file
  ## Overview
This Postman collection contains API requests for verifying shipment details and addresses using the EasyPost API. The collection includes test scripts to validate API responses.

## Collection Information
- **Postman ID:** 9953a316-91b0-4149-8715-d6c78fe87a95
- **Name:** Impledge_QA_VANSHIKA KANSAL
- **Schema Version:** v2.1.0
- **Exporter ID:** 42233723

## API Endpoints

### 1. Get Shipment Details
**Method:** GET  
**URL:** `https://api.easypost.com/v2/shipments/shp_e0b570fd1d7d4b62bd206917eae5881a`  
**Description:** Fetches details of a specific shipment.

**Tests:**
- Verify that `selected_rate.retail_rate` is equal to `12.00`.
- Ensure `retail_rate` is greater than `list_rate`.

### 2. Address Verification
**Method:** POST  
**URL:** `https://api.easypost.com/v2/addresses?verify_strict[]=delivery`  
**Description:** Verifies the provided address for delivery accuracy.

**Request Body (JSON):**
```json
{
    "company": "Residence Inn",
    "street1": "22 Segar St",
    "street2": "",
    "city": "Danbury",
    "country": "US",
    "phone": "855-782-3877",
    "zip": "06810",
    "email": "shipper@mailinator.com"
}
```

**Tests:**
- Ensure response body contains no errors.
- Verify that the ZIP code `06810` is present in the response.

## Authentication
- **Type:** Basic Authentication
- **Username:** `EZTK0126bfcd0c834208b2289e3c501630d7IMAAxVrGZ2G1UXCmomm4Pw`

## Setup Instructions
1. Import this collection into Postman.
2. Ensure the EasyPost API key is correctly set in the authentication.
3. Run requests and verify test results.

## Notes
- The `Authorization` header in the Address Verification request is currently disabled.
- Adjust request parameters as needed for different test cases.

## Dependencies
- Postman v9+ (Recommended)
- Active EasyPost API credentials

## License
This collection is intended for QA and testing purposes only.

                                                             SQL readme file
  ## Instructions

### Step 1: Open SQL Practice Tool
1. Open the **Google Chrome** browser.
2. Go to [SQL Practice](https://www.sql-practice.com/).
3. Click on **SQL Database** on the left-hand side.
4. Click on **View Schema** to understand the relationships between `patients`, `doctors`, and `admissions` tables.

### Step 2: Execute Preliminary Update Queries
Before running the **SELECT** queries, execute the following **UPDATE** statements to modify the `admissions` table:

```sql
UPDATE Admissions SET attending_doctor_id = 29 WHERE attending_doctor_id = 3;
UPDATE Admissions SET patient_id = 4 WHERE patient_id = 35;
```

### Step 3: Execute SQL Test Queries

Now, solve the following SQL problems **without using specific clauses for `attending_doctor_id` or `patient_id`** (e.g., `attending_doctor_id != 1`, `patient_id = 2`, etc.).

#### Query 1: Select details of Doctors who have Admissions
```sql
SELECT DISTINCT d.*
FROM Doctors d
JOIN Admissions a ON d.doctor_id = a.attending_doctor_id;
```

#### Query 2: Select details of Doctors who have no Admissions
```sql
SELECT d.*
FROM Doctors d
LEFT JOIN Admissions a ON d.doctor_id = a.attending_doctor_id
WHERE a.attending_doctor_id IS NULL;
```

#### Query 3: Select details of Patients whose Admission can’t be completed due to missing doctor details
```sql
SELECT p.*
FROM Patients p
JOIN Admissions a ON p.patient_id = a.patient_id
LEFT JOIN Doctors d ON a.attending_doctor_id = d.doctor_id
WHERE d.doctor_id IS NULL;
```

## Notes
- Ensure that the **UPDATE** queries are executed before running the **SELECT** queries.
- Avoid hardcoding specific values like `attending_doctor_id=3` or `patient_id=4` in the **SELECT** queries.
- Use **JOINs** and **NULL checks** to get the required results dynamically.

Happy Querying!

                                                           
                                                                          
