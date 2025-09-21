# tests/test_ingest.py
from src.ingest import parse_rss

URL = "https://www.google.com/alerts/feeds/15937600743486598571/379441454725237454"  # <-- your URL
rows = list(parse_rss(URL, "Europe/London"))
print("Items:", len(rows))
print(rows[0] if rows else "No entries yet")

# Items: 1
# {'id': '42c3836c32b697e6b5ec5794fcd3d5459ddfd12f', 'title': '<b>Trainee</b> Dental Nurse - <b>Newcastle upon Tyne</b> NE5 2LH - Indeed.com', 'url': 'https://www.gow.google.com/url?rct=j&sa=t&url=https://uk.indeed.com/viewjob%3Fjk%3D9ea3acf639d638fb&ct=ga&cd=CAIyHjFlZjhkYzU0ZTNmMjE3NzA6Y28udWs6ZW46R0I6Ug&usg=AOvVaw03a4XB61z97G1hzg9W7WAiij2k', 'snippet': '<b>Trainee</b> Dental Nurse. The Dental Care Clinic, Westerhope, <b>Newcastle</b>. <b>Newcastle upon Tyne</b> NE5 2LH. &amp;nbsp;<J<>. <b>Job</b> details. Pay. From £12.21 an hour. <b>Job</b>&nbsp;...', 'published_at': datetime.datetime(2025, 9, 21, 1, 28, 18, tzinfo=tzfile('GB-Eire')), 'sou'hswrce': 'https://www.google.com/alerts/feeds/15937600743486598571/379441454725237454'}