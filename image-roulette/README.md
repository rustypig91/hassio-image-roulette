# Home Assistant Add-on: Image roulette

## About

Serve a random image from specified folder.

## Custom HTML

Custom html can be used to add e.g. overlay to display the current time or similar.
To use a custom url set the `Templates folder` option to a path containing `index.html` e.g. `/media/`
This should be folder containing flask templates. Use the following as a baseline for index.html.


```html<html>
<head>
    {{ header|safe }}
</head>
<body>
</body>
</html>
```

`{{ header|safe }}` will insert the neccessary stuff for displaying random images as background.
