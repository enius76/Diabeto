(function(e, t, n) {
    "use strict";
    e.Calendario = function(t, n) {
        this.$el = e(n);
        this._init(t)
    };
    e.Calendario.defaults = {
        weeks: ["Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi", "Dimanche"],
        weekabbrs: ["Lun", "Mar", "Mer", "Jeu", "Ven", "Sam", "Dim"],
        months: ["Janvier", "Février", "Mars", "Avril", "Mai", "Juin", "Juillet", "Août", "Septembre", "Octobre", "Novembre", "Décembre"],
        monthabbrs: ["Jan", "Fév", "Mars", "Avr", "Mai", "Juin", "Juil", "Août", "Sept", "Oct", "Nov", "Dec"],
        displayWeekAbbr: false,
        displayMonthAbbr: false,
        startIn: 1,
        events: "click",
        fillEmpty: true,
        feedParser: "./feed/",
        zone: "00:00",
        checkUpdate: true
    };
    e.Calendario.prototype = {
        _init: function(t) {
            this.VERSION = "3.2.0";
            this.UNIQUE = "%{unique}%";
            this.options = e.extend(true, {}, e.Calendario.defaults, t);
            this.today = new Date;
            this.month = isNaN(this.options.month) || this.options.month === null ? this.today.getMonth() : this.options.month - 1;
            this.year = isNaN(this.options.year) || this.options.year === null ? this.today.getFullYear() : this.options.year;
            this.caldata = this._processCaldata(this.options.caldata);
            if (parseFloat(e().jquery) >= 1.9 && this.options.events.indexOf("hover") != -1) this.logError("'hover' psuedo-name is not supported" + " in jQuery 1.9+. Use 'mouseenter' 'mouseleave' events instead.");
            this.options.events = this.options.events.split(",");
            this.options.zone = this.options.zone.charAt(0) != "+" && this.options.zone.charAt(0) != "-" ? "+" + this.options.zone : this.options.zone;
            this._generateTemplate(true);
            this._initEvents()
        },
        _processCaldataObj: function(t, r) {
            if (typeof t !== "object") t = {
                content: t,
                startTime: "00:00",
                endTime: "23:59",
                allDay: true
            };
            if (!t.content) this.logError("Content is missing in date " + r);
            if (t.startTime && !t.endTime) t.endTime = parseInt(t.startTime.split(":")[0]) + 1 + ":" + t.startTime.split(":")[1];
            if (!t.startTime && !t.endTime) t = e.extend({}, t, {
                startTime: "00:00",
                endTime: "23:59",
                allDay: true
            });
            if (t.startTime && t.endTime && t.allDay === n) t.allDay = false;
            if (/^\d{2}-DD-\d{4}/.test(r) || /^\d{2}-DD-YYYY/.test(r)) {
                var i = /^(\d{2})-DD-(\d{4})/.exec(r) || /^(\d{2})-DD-YYYY/.exec(r),
                    s;
                if (i.length == 3) s = new Date(i[2], i[1], 0);
                else if (i.length == 2) s = new Date(this.year, i[1], 0);
                if (!t.startDate) t.startDate = 1;
                if (!t.endDate && s.getDate() != 1) t.endDate = s.getDate();
                if (!t.endDate && s.getDate() == 1 && i.length == 3) t.endDate = s.getDate()
            }
            return t
        },
        _processCaldata: function(t) {
            var n = this;
            t = t || {};
            e.each(t, function(r, i) {
                if (/^\d{2}-\d{2}-\d{4}/.test(r) || /^\d{2}-\d{2}-YYYY/.test(r) || /^\d{2}-DD-YYYY/.test(r) || /^MM-\d{2}-YYYY/.test(r) || /^\d{2}-DD-YYYY/.test(r) || /^MM-\d{2}-\d{4}/.test(r) || /^\d{2}-DD-\d{4}/.test(r) || r == "TODAY") {} else n.logError(r + " is an Invalid Date. Date should not contain spaces, should be separated by '-' and should be in the " + "format 'MM-DD-YYYY'. That ain't that difficult!"); if (Array.isArray(i)) {
                    e.each(i, function(e, t) {
                        i[e] = n._processCaldataObj(t, r)
                    });
                    t[r] = i
                } else {
                    t[r] = n._processCaldataObj(i, r)
                }
            });
            return t
        },
        _propDate: function(t, n) {
            var r = t.index(),
                i = {
                    allDay: [],
                    content: [],
                    endTime: [],
                    startTime: []
                }, s = {
                    day: t.children("span.fc-date").text(),
                    month: this.month + 1,
                    monthname: this.options.displayMonthAbbr ? this.options.monthabbrs[this.month] : this.options.months[this.month],
                    year: this.year,
                    weekday: r + this.options.startIn,
                    weekdayname: this.options.weeks[r == 6 ? 0 : r + this.options.startIn]
                };
            t.children("div.fc-calendar-events").children("div.fc-calendar-event").each(function(t, n) {
                var r = e("<div>" + e(n).html() + "</div>");
                i.startTime[t] = new Date(r.find("time.fc-starttime").attr("datetime"));
                i.endTime[t] = new Date(r.find("time.fc-endtime").attr("datetime"));
                i.allDay[t] = r.find("time.fc-allday").attr("datetime") === "true" ? true : false;
                r.find("time").remove();
                i.content[t] = r.html()
            });
            if (s.day) this.options[n](t, i, s)
        },
        _initEvents: function() {
            var t = this,
                r = [],
                i = [];
            for (var s = 0; s < t.options.events.length; s++) {
                r[s] = t.options.events[s].toLowerCase().trim();
                i[s] = "onDay" + r[s].charAt(0).toUpperCase() + r[s].slice(1);
                if (this.options[i[s]] === n) this.options[i[s]] = function(e, t, n) {
                    return false
                };
                this.$el.on(r[s] + ".calendario", "div.fc-row > div", function(n) {
                    if (n.type == "mouseenter" || n.type == "mouseleave") n.type = e.inArray(n.type, r) == -1 ? "hover" : n.type;
                    t._propDate(e(this), i[e.inArray(n.type, r)])
                })
            }
            this.$el.on("shown.calendar.calendario", function(e, n) {
                if (n && n.options.checkUpdate) t._checkUpdate()
            });
            this.$el.delay(new Date(this.today.getFullYear(), this.today.getMonth(), this.today.getDate() + 1, 0, 0, 0) - (new Date).getTime()).queue(function() {
                t.today = new Date;
                if (t.today.getMonth() == t.month || t.today.getMonth() + 1 == t.month) t._generateTemplate(true);
                t.$el.trigger(e.Event("newday.calendar.calendario"))
            })
        },
        _checkUpdate: function() {
            var t = this;
            e.getScript("https://raw.githubusercontent.com/codrops/Calendario/master/js/update.js").done(function(e, n) {
                if (calendario.current != t.version() && parseFloat(calendario.current) >= parseFloat(t.version())) console.info(calendario.msg)
            }).fail(function(e, t, n) {
                console.error(n)
            })
        },
        _generateTemplate: function(t, n) {
            var r = this._getHead(),
                i = this._getBody(),
                s;
            switch (this.rowTotal) {
                case 4:
                    s = "fc-four-rows";
                    break;
                case 5:
                    s = "fc-five-rows";
                    break;
                case 6:
                    s = "fc-six-rows";
                    break
            }
            this.$cal = e('<div class="fc-calendar ' + s + '">').append(r, i);
            this.$el.find("div.fc-calendar").remove().end().append(this.$cal);
            this.$el.find(".fc-emptydate").parent().css({
                background: "transparent",
                cursor: "default"
            });
            if (!t) this.$el.trigger(e.Event("shown.calendario"));
            if (n) n.call()
        },
        _getHead: function() {
            var e = '<div class="fc-head">';
            for (var t = 0; t <= 6; t++) {
                var n = t + this.options.startIn,
                    r = n > 6 ? n - 6 - 1 : n;
                e += "<div>" + (this.options.displayWeekAbbr ? this.options.weekabbrs[r] : this.options.weeks[r]) + "</div>"
            }
            return e + "</div>"
        },
        _parseDataToDay: function(e, t, n) {
            var r = "";
            if (!n) {
                if (Array.isArray(e)) r = this._convertDayArray(e, t);
                else r = this._wrapDay(e, t, true)
            } else {
                if (!Array.isArray(e)) e = [e];
                for (var i = 0; i < e.length; i++) {
                    if (this.month != 1 && t >= e[i].startDate && t <= e[i].endDate) r += this._wrapDay(e[i], t, true);
                    else if (this.month == 1 && t >= e[i].startDate) {
                        if (e[i].endDate && t <= e[i].endDate) r += this._wrapDay(e[i], t, true);
                        else if (!e[i].endDate) r += this._wrapDay(e[i], t, true)
                    }
                }
            }
            return r
        },
        _toDateTime: function(e, t, n) {
            var r = parseInt(this.options.zone.split(":")[0]),
                i = parseInt(this.options.zone.charAt(0) + this.options.zone.split(":")[1]),
                s = parseInt(e.split(":")[0]) - r,
                o = parseInt(e.split(":")[1]) - i,
                u = new Date(Date.UTC(this.year, this.month, t, s, o, 0, 0));
            if (n) {
                var a = parseInt(n.split(":")[0]) - r,
                    f = parseInt(n.split(":")[1]) - i;
                if (u.getTime() - (new Date(Date.UTC(this.year, this.month, t, a, f, 0, 0))).getTime() < 0) u = new Date(Date.UTC(this.year, this.month, t + 1, s, o, 0, 0))
            }
            return u.toISOString()
        },
        _timeHtml: function(e, t) {
            var n = e.content;
            n += '<time class="fc-allday" datetime="' + e.allDay + '"></time>';
            n += '<time class="fc-starttime" datetime="' + this._toDateTime(e.startTime, t) + '">' + e.startTime + "</time>";
            n += '<time class="fc-endtime" datetime="' + this._toDateTime(e.endTime, t, e.startTime) + '">' + e.endTime + "</time>";
            return n
        },
        _wrapDay: function(e, t, n) {
            if (t) {
                if (n) return '<div class="fc-calendar-event">' + this._timeHtml(e, t) + "</div>";
                else return this._timeHtml(e, t)
            } else return '<div class="fc-calendar-event">' + e + "</div>"
        },
        _convertDayArray: function(e, t) {
            for (var n = 0; n < e.length; n++) {
                e[n] = this._wrapDay(e[n], t, false)
            }
            return this._wrapDay(e.join('</div><div class="fc-calendar-event">'))
        },
        _getBody: function() {
            var e = new Date(this.year, this.month + 1, 0),
                t = e.getDate(),
                n = new Date(this.year, e.getMonth(), 1),
                r = (new Date(this.year, this.month, 0)).getDate();
            this.startingDay = n.getDay();
            var i = '<div class="fc-body"><div class="fc-row">',
                s = 1;
            for (var o = 0; o < 7; o++) {
                for (var u = 0; u <= 6; u++) {
                    var a = this.startingDay - this.options.startIn,
                        f = a < 0 ? 6 + a + 1 : a,
                        l = "",
                        c = this.month === this.today.getMonth() && this.year === this.today.getFullYear() && s === this.today.getDate(),
                        h = this.year < this.today.getFullYear() || this.month < this.today.getMonth() && this.year === this.today.getFullYear() || this.month === this.today.getMonth() && this.year === this.today.getFullYear() && s < this.today.getDate(),
                        p = "";
                    if (this.options.fillEmpty && (u < f || o > 0)) {
                        if (s > t) {
                            l = '<span class="fc-date fc-emptydate">' + (s - t) + '</span><span class="fc-weekday">';
                            ++s
                        } else if (s == 1) {
                            l = '<span class="fc-date fc-emptydate">' + (r - f + 1) + '</span><span class="fc-weekday">';
                            ++r
                        }
                        l += this.options.weekabbrs[u + this.options.startIn > 6 ? u + this.options.startIn - 6 - 1 : u + this.options.startIn] + "</span>"
                    }
                    if (s <= t && (o > 0 || u >= f)) {
                        l = '<span class="fc-date">' + s + '</span><span class="fc-weekday">' + this.options.weekabbrs[u + this.options.startIn > 6 ? u + this.options.startIn - 6 - 1 : u + this.options.startIn] + "</span>";
                        var d = (this.month + 1 < 10 ? "0" + (this.month + 1) : this.month + 1) + "-" + (s < 10 ? "0" + s : s) + "-" + this.year,
                            v = this.caldata[d],
                            m = (this.month + 1 < 10 ? "0" + (this.month + 1) : this.month + 1) + "-" + (s < 10 ? "0" + s : s) + "-YYYY",
                            g = this.caldata[m],
                            y = "MM-" + (s < 10 ? "0" + s : s) + "-" + this.year,
                            b = this.caldata[y],
                            w = "MM" + "-" + (s < 10 ? "0" + s : s) + "-YYYY",
                            E = this.caldata[w],
                            S = (this.month + 1 < 10 ? "0" + (this.month + 1) : this.month + 1) + "-DD-" + this.year,
                            x = this.caldata[S],
                            T = (this.month + 1 < 10 ? "0" + (this.month + 1) : this.month + 1) + "-DD-YYYY",
                            N = this.caldata[T];
                        if (c && this.caldata.TODAY) p += this._parseDataToDay(this.caldata.TODAY, s);
                        if (v) p += this._parseDataToDay(v, s);
                        if (b) p += this._parseDataToDay(b, s);
                        if (x) p += this._parseDataToDay(x, s, true);
                        if (N) p += this._parseDataToDay(N, s, true);
                        if (E) p += this._parseDataToDay(E, s);
                        if (g) p += this._parseDataToDay(g, s);
                        if (p !== "") l += '<div class="fc-calendar-events">' + p + "</div>";
                        ++s
                    } else {
                        c = false
                    }
                    var C = c ? "fc-today " : "";
                    if (h) C += "fc-past ";
                    else C += "fc-future "; if (p !== "") C += "fc-content";
                    i += (C !== "" ? '<div class="' + C.trim() + '">' : "<div>") + l + "</div>"
                }
                if (s > t) {
                    this.rowTotal = o + 1;
                    break
                } else {
                    i += '</div><div class="fc-row">'
                }
            }
            return i + "</div></div>"
        },
        _move: function(e, t, n) {
            if (t === "previous") {
                if (e === "month") {
                    this.year = this.month > 0 ? this.year : --this.year;
                    this.month = this.month > 0 ? --this.month : 11
                } else if (e === "year") this.year = --this.year
            } else if (t === "next") {
                if (e === "month") {
                    this.year = this.month < 11 ? this.year : ++this.year;
                    this.month = this.month < 11 ? ++this.month : 0
                } else if (e === "year") this.year = ++this.year
            }
            this._generateTemplate(false, n)
        },
        option: function(e, t) {
            if (t) this.options[e] = t;
            else return this.options[e]
        },
        getYear: function() {
            return this.year
        },
        getMonth: function() {
            return this.month + 1
        },
        getMonthName: function() {
            return this.options.displayMonthAbbr ? this.options.monthabbrs[this.month] : this.options.months[this.month]
        },
        getCell: function(e) {
            var t = Math.floor((e + this.startingDay - this.options.startIn - 1) / 7),
                n = e + this.startingDay - this.options.startIn - t * 7 - 1;
            return this.$cal.find("div.fc-body").children("div.fc-row").eq(t).children("div").eq(n)
        },
        setData: function(t, n) {
            t = this._processCaldata(t);
            if (n) this.caldata = t;
            else e.extend(this.caldata, t);
            this._generateTemplate(false)
        },
        gotoNow: function(e) {
            this.month = this.today.getMonth();
            this.year = this.today.getFullYear();
            this._generateTemplate(false, e)
        },
        gotoMonth: function(e, t, n) {
            this.month = e - 1;
            this.year = t;
            this._generateTemplate(false, n)
        },
        gotoPreviousMonth: function(e) {
            this._move("month", "previous", e)
        },
        gotoPreviousYear: function(e) {
            this._move("year", "previous", e)
        },
        gotoNextMonth: function(e) {
            this._move("month", "next", e)
        },
        gotoNextYear: function(e) {
            this._move("year", "next", e)
        },
        feed: function(t) {
            var n = this;
            e.post(n.options.feedParser, {
                dates: this.caldata
            }).always(function(e) {
                if (t) t.call(this, JSON.parse(e).hevent)
            })
        },
        version: function() {
            return this.VERSION
        }
    };
    var r = function(e) {
        throw new Error(e)
    };
    e.fn.calendario = function(t) {
        var n = e.data(this, "calendario");
        if (typeof t === "string") {
            var i = Array.prototype.slice.call(arguments, 1);
            this.each(function() {
                if (!n) {
                    r("Cannot call methods on calendario prior to initialization; Attempted to call method '" + t + "'");
                    return
                }
                if (!e.isFunction(n[t]) || t.charAt(0) === "_") {
                    r("No such method '" + t + "' for calendario instance.")
                }
                n[t].apply(n, i)
            })
        } else {
            this.each(function() {
                if (n) n._init();
                else n = e.data(this, "calendario", new e.Calendario(t, this))
            })
        }
        n.$el.trigger(e.Event("shown.calendar.calendario"), [n]);
        return n
    }
})(jQuery, window)
