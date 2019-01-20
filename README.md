# PostEmbeds
This basic Flask app demonstrates and tests one possible approach at implementing a Facebook-like URL previewing functionality when users type/enter a link into a form field.

To make this happen, the approach used in this app follows the below steps:

1. Use JQuery to listen for user input on a specified field
2. Find and extract URL using regex
3. Send an Ajax get request to a Flask view with extracted URL as query parameter
4. Obtain OpenGraph/Twitter Card/page summary of the URL
5. Render a short HTML snippet for displaying the summary details
6. Return the HTML snippet as a JSON object (as the return result to the above get request)
7. Append the HTML snippet to the designated output div

The generated HTML snippet for the URL preview is also stored in the value attribute in a hidden input tag. This allows the app to retrieve the snippet once the user submits the form, so that we can do things like persisting the snippet into a database column or passing it as argument to another view.

## Dependencies
This was built with Flask 1.0.2 and tested on Python 3.6. The app does the bulk of the summary/detail extraction using the [webpreview](https://github.com/ludbek/webpreview) package.

Please see the project's requirements.txt file for a full list of dependencies.

## Resources
The approach used in this app adopts and combines ideas suggested in the following resources:

* [Extract URL Data Like Facebook Using PHP,jQuery And Ajax.](http://talkerscode.com/webtricks/extract-url-data-like-facebook-using-php-jquery-and-ajax.php)
* [Facebook Like Extracting URL Data with Jquery and Ajax](https://www.9lessons.info/2010/06/facebook-like-extracting-url-data-with.html)
* [how to create URL extractor like facebook share](https://stackoverflow.com/questions/2999535/how-to-create-url-extractor-like-facebook-share)

The loading icon/animation comes from [Preloaders.net](https://icons8.com/preloaders/)

## License
[MIT License](https://opensource.org/licenses/MIT)

## Contributing
Please feel free to use or build this project further.
