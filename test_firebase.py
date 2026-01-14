from firebase import ref

ref.push({
    "name": "TEST",
    "lat": "1",
    "lng": "2",
    "emergency": "Test",
    "time": "now"
})

print("Data sent")
