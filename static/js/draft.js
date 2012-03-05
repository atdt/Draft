(function (exports) {
    var debug = document.getElementsByTagName('pre')[0];

    exports.log = function () {
        var args = Array.prototype.slice.call(arguments, 0),
            code = document.createElement('code');

        code.textContent = args.reduce(function (p, c) {
            return [p, c.toString()].join(' ');
        });

        el.appendChild(code);
    };
})(this);
