from canadapostwrapper import CanadaPostTracker

def main():
    tracking_id = '6107031730947239'
    tracker = CanadaPostTracker(tracking_id=tracking_id)
    shipping_info = tracker.check_shipping()
    if shipping_info:
        print("Initial Shipping Info:")
        print(shipping_info)
    print("Started continuous tracking.")
    tracker.start_tracking()

if __name__ == "__main__":
    main()
