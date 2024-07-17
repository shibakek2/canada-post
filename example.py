from canadapostwrapper.canadapost import CanadaPostTracker

tracker = CanadaPostTracker(tracking_id='YOUR_TRACKING_ID')

shipping_info = tracker.check_shipping()

if shipping_info:
    print(shipping_info)
else:
    print("Failed to retrieve shipping information.")
