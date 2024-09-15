# Home Assistant Add-on: Image roulette

## About

Serve a random image from specified folder.

## Custom HTML

A custom html can be used to add e.g. overlay to display the current time or similar.
To use a custom url set the `Custom html` option to the html path e.g. `/media/custom.html`
Use this template to start working on the custom.html


```html<html>
<head>
    {{ header|safe }}
</head>
<body>
</body>
</html>
```

`{{ header|safe }}` will insert the neccessary stuff for displaying random images as background.
