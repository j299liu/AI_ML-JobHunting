# tests/test_dedupe.py
from src.dedupe import near_duplicate

a = {"title": "Trainee Dental Nurse", "company": "The Dental Care Clinic, Westerhope, Newcastle", "location": "Newcastle upon Tyne NE5 2LH", "url": "https://uk.indeed.com/viewjob?jk=9ea3acf639d638fb"}
b = {"title": "Dental Receptionist Apprenticeship (Customer Service) - Newcastle", "company": "RIVERDALE TRADECO LIMITED", "location": "Newcastle Upon Tyne, Tyne and Wear", "url": "https://www.totaljobs.com/job/dental-receptionist-apprenticeship-customer-service-newcastle/riverdale-tradeco-limited-job105824323"}
c = {"title": "Dental Receptionist Apprenticeship (Customer Service) - Newcastle", "company": "RIVERDALE TRADECO LIMITED", "location": "Newcastle upon Tyne NE3 2DQ", "url": "https://uk.indeed.com/viewjob?jk=9e17beba56ffb3a2"}

print("a~b?", near_duplicate(a,b))
print("b~c?", near_duplicate(b,c)) 