var customizer = (function(window, undefined) {

    function buildWg(options, css) {

        // Add styles
        addStyles(!!css ? css : 'customizer/main.css');

        var style = '-webkit-transform: translate(-260px, 0); -moz-transform: translate(-260px, 0); -ms-transform: translate(-260px, 0); -o-transform: translate(-260px, 0);';

        // Make markup
        var $wg = $('<div class="b-customizer" style="' + style + '"></div>'),

            $toggle = $('<a href="javascript:void(0)" class="b-customizer_toggle i-icon"><i class="fa icon fa-cog fa-spin"></i></a>'),
            $box = $('<div class="b-customizer_options"></div>');

        $.each(options, function(key, val) {

            var $set = $('<div class="b-customizer_set"></div>'),
                $title = $('<div class="b-customizer_set_legend">' + this.title + '</div>'),
                $list = $('<ul class="b-customizer_' + key + '"></ul>');

            $.each(this.options, function() {

                var current = !!this[3] ? ' current' : '';

                $('<li><a href="' + this[1] + '" class="' + this[0] + current + '">' + this[2] + '</a></li>').appendTo($list);

            });

            $title.appendTo($set);
            $list.appendTo($set);

            $set.appendTo($box);

        });

        $toggle.appendTo($wg);
        $box.appendTo($wg);

        $('body').append($wg);

        // Add events listeners
        togglePanel.call($toggle, $wg);
        colors();
        typography();

    }

    function togglePanel($wg) {

        this.on('click', function(e) {

            $wg.attr('style', '');
            $wg.toggleClass('open');

        });

       /* $(document).bind('click.customizeClose', function(e) {

            var $target = $(e.target),
                targetIsNavItem = $target.hasClass('b-customizer') || $target.closest('.b-customizer').length;

            if (!targetIsNavItem) {

                $wg.toggleClass('open', false);

            }

        });*/

    }

    function colors() {

        var $links = $('.b-customizer_colors a');

        $links.on('click', function(e) {

            e.preventDefault();

            $links.removeClass('current');
            $(this).addClass('current');

            $('#color-scheme').attr('href', $(this).attr('href'));

        });

    }
    function typography() {

        var $links = $('.b-customizer_typography a');

        $links.on('click', function(e) {

            e.preventDefault();

            $links.removeClass('current');
            $(this).addClass('current');

            $('#typography-scheme').attr('href', $(this).attr('href'));

        });

    }

    function addStyles(url) {

        var cssId = 'myCss';

        if (!document.getElementById(cssId)) {

            var head  = document.getElementsByTagName('head')[0],
                link  = document.createElement('link');

            link.id   = cssId;
            link.rel  = 'stylesheet';
            link.type = 'text/css';
            link.href = url;
            link.media = 'all';

            head.appendChild(link);

        }

    }

    return {
        init: function(options, css) {

            // Build widget
            buildWg(options, css);

        }
    };

})(window);