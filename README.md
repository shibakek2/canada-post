# CanadaPostWrapper

CanadaPostWrapper is a Python package that allows you to track packages using Canada Post's tracking service.

## Installation

You can install the package using pip:

pip install canadapostwrapper


## Usage


### Parameters

- `tracking_id` (str): The tracking ID of the package you want to track.
- `delay` (int, optional): The delay in minutes between each tracking check. Default is 1 minute.

### Methods

#### `check_shipping()`

Checks the current shipping status of the package.

**Returns:**
- A dictionary containing the shipping information if the status has changed since the last check.
- `None` if there is no change in status or if an error occurs.

#### `start_tracking()`

Starts continuous tracking of the package. This method will print the shipping information to the console every `delay` minutes.

## Example

Initialize the tracker

tracker = CanadaPostTracker(tracking_id='123456789012')

## Check the shipping status once

shipping_info = tracker.check_shipping()
if shipping_info:
    print(shipping_info)

## Start continuous tracking

tracker.start_tracking()    



## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request on GitHub.

## Author

Your Name - [wilhemnorman732@gmail.com](mailto:wilhemnorman732@gmail.com)

## Acknowledgments

- Thanks to Canada Post for providing the tracking service.
