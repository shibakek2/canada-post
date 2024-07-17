# Canada Post Wrapper

A Python wrapper for tracking packages with Canada Post.

## Installation

You can install the package using pip:

pip install canadapostwrapper


## Usage

Here’s an example of how to use the `CanadaPostTracker` class to track a package:


python

Replace 'YOUR_TRACKING_ID' with your actual tracking ID

from canadapostwrapper.canadapost import CanadaPostTracker
tracker = CanadaPostTracker(tracking_id='YOUR_TRACKING_ID')
tracker.start_tracking()

### Example Output

The `start_tracking` method will continuously check the status of your package and print the shipping information:


json
{
"Sent From": "Origin Information",
"Shipping To": "Destination Information",
"Status": "ITEM PICKED UP BY CARRIER",
"Expected Delivery Date": "Friday, October 15, 2021",
"Tracking Number": "YOUR_TRACKING_ID",
"Status Detail": "Detailed Status Information"
}

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

If you would like to contribute to this project, please fork the repository and submit a pull request.

## Author

shibakek - [wilhemnorman732@gmail.com](mailto:wilhemnorman732@gmail.co)

## Acknowledgments

- Thanks to the developers of the `requests` library for making HTTP requests in Python easy.
