(function () {
  var collect = (function (t) {
    var r = {};
    function e(n) {
      if (r[n]) return r[n].exports;
      var i = (r[n] = { i: n, l: !1, exports: {} });
      return t[n].call(i.exports, i, i.exports, e), (i.l = !0), i.exports;
    }
    return (
      (e.m = t),
      (e.c = r),
      (e.d = function (t, r, n) {
        e.o(t, r) || Object.defineProperty(t, r, { enumerable: !0, get: n });
      }),
      (e.r = function (t) {
        "undefined" != typeof Symbol &&
          Symbol.toStringTag &&
          Object.defineProperty(t, Symbol.toStringTag, { value: "Module" }),
          Object.defineProperty(t, "__esModule", { value: !0 });
      }),
      (e.t = function (t, r) {
        if ((1 & r && (t = e(t)), 8 & r)) return t;
        if (4 & r && "object" == typeof t && t && t.__esModule) return t;
        var n = Object.create(null);
        if (
          (e.r(n),
          Object.defineProperty(n, "default", { enumerable: !0, value: t }),
          2 & r && "string" != typeof t)
        )
          for (var i in t)
            e.d(
              n,
              i,
              function (r) {
                return t[r];
              }.bind(null, i)
            );
        return n;
      }),
      (e.n = function (t) {
        var r =
          t && t.__esModule
            ? function () {
                return t.default;
              }
            : function () {
                return t;
              };
        return e.d(r, "a", r), r;
      }),
      (e.o = function (t, r) {
        return Object.prototype.hasOwnProperty.call(t, r);
      }),
      (e.p = ""),
      e((e.s = 10))
    );
  })([
    function (t, r, e) {
      "use strict";
      function n(t) {
        return (n =
          "function" == typeof Symbol && "symbol" == typeof Symbol.iterator
            ? function (t) {
                return typeof t;
              }
            : function (t) {
                return t &&
                  "function" == typeof Symbol &&
                  t.constructor === Symbol &&
                  t !== Symbol.prototype
                  ? "symbol"
                  : typeof t;
              })(t);
      }
      t.exports = {
        isArray: function (t) {
          return Array.isArray(t);
        },
        isObject: function (t) {
          return "object" === n(t) && !1 === Array.isArray(t) && null !== t;
        },
        isFunction: function (t) {
          return "function" == typeof t;
        },
      };
    },
    function (t, r, e) {
      "use strict";
      function n(t) {
        return (
          (function (t) {
            if (Array.isArray(t)) return i(t);
          })(t) ||
          (function (t) {
            if (
              ("undefined" != typeof Symbol && null != t[Symbol.iterator]) ||
              null != t["@@iterator"]
            )
              return Array.from(t);
          })(t) ||
          (function (t, r) {
            if (!t) return;
            if ("string" == typeof t) return i(t, r);
            var e = Object.prototype.toString.call(t).slice(8, -1);
            "Object" === e && t.constructor && (e = t.constructor.name);
            if ("Map" === e || "Set" === e) return Array.from(t);
            if (
              "Arguments" === e ||
              /^(?:Ui|I)nt(?:8|16|32)(?:Clamped)?Array$/.test(e)
            )
              return i(t, r);
          })(t) ||
          (function () {
            throw new TypeError(
              "Invalid attempt to spread non-iterable instance.\nIn order to be iterable, non-array objects must have a [Symbol.iterator]() method."
            );
          })()
        );
      }
      function i(t, r) {
        (null == r || r > t.length) && (r = t.length);
        for (var e = 0, n = new Array(r); e < r; e++) n[e] = t[e];
        return n;
      }
      t.exports = function (t) {
        var r = [];
        return (
          Array.isArray(t)
            ? r.push.apply(r, n(t))
            : "Collection" === t.constructor.name
            ? r.push.apply(r, n(t.all()))
            : Object.keys(t).forEach(function (e) {
                return r.push(t[e]);
              }),
          r
        );
      };
    },
    function (t, r, e) {
      "use strict";
      t.exports = function (t, r) {
        try {
          return r.split(".").reduce(function (t, r) {
            return t[r];
          }, t);
        } catch (r) {
          return t;
        }
      };
    },
    function (t, r, e) {
      "use strict";
      t.exports = function (t) {
        return Array.isArray(t[0]) ? t[0] : t;
      };
    },
    function (t, r, e) {
      "use strict";
      var n = e(0).isFunction;
      t.exports = function (t) {
        return void 0 === t
          ? this.sum() / this.items.length
          : n(t)
          ? new this.constructor(this.items).sum(t) / this.items.length
          : new this.constructor(this.items).pluck(t).sum() / this.items.length;
      };
    },
    function (t, r, e) {
      "use strict";
      function n(t) {
        return (
          (function (t) {
            if (Array.isArray(t)) return i(t);
          })(t) ||
          (function (t) {
            if (
              ("undefined" != typeof Symbol && null != t[Symbol.iterator]) ||
              null != t["@@iterator"]
            )
              return Array.from(t);
          })(t) ||
          (function (t, r) {
            if (!t) return;
            if ("string" == typeof t) return i(t, r);
            var e = Object.prototype.toString.call(t).slice(8, -1);
            "Object" === e && t.constructor && (e = t.constructor.name);
            if ("Map" === e || "Set" === e) return Array.from(t);
            if (
              "Arguments" === e ||
              /^(?:Ui|I)nt(?:8|16|32)(?:Clamped)?Array$/.test(e)
            )
              return i(t, r);
          })(t) ||
          (function () {
            throw new TypeError(
              "Invalid attempt to spread non-iterable instance.\nIn order to be iterable, non-array objects must have a [Symbol.iterator]() method."
            );
          })()
        );
      }
      function i(t, r) {
        (null == r || r > t.length) && (r = t.length);
        for (var e = 0, n = new Array(r); e < r; e++) n[e] = t[e];
        return n;
      }
      t.exports = function (t) {
        var r, e;
        Array.isArray(t)
          ? (e = r = []).push.apply(e, n(t))
          : ((r = {}),
            Object.keys(t).forEach(function (e) {
              r[e] = t[e];
            }));
        return r;
      };
    },
    function (t, r, e) {
      "use strict";
      function n(t) {
        return (
          (function (t) {
            if (Array.isArray(t)) return i(t);
          })(t) ||
          (function (t) {
            if (
              ("undefined" != typeof Symbol && null != t[Symbol.iterator]) ||
              null != t["@@iterator"]
            )
              return Array.from(t);
          })(t) ||
          (function (t, r) {
            if (!t) return;
            if ("string" == typeof t) return i(t, r);
            var e = Object.prototype.toString.call(t).slice(8, -1);
            "Object" === e && t.constructor && (e = t.constructor.name);
            if ("Map" === e || "Set" === e) return Array.from(t);
            if (
              "Arguments" === e ||
              /^(?:Ui|I)nt(?:8|16|32)(?:Clamped)?Array$/.test(e)
            )
              return i(t, r);
          })(t) ||
          (function () {
            throw new TypeError(
              "Invalid attempt to spread non-iterable instance.\nIn order to be iterable, non-array objects must have a [Symbol.iterator]() method."
            );
          })()
        );
      }
      function i(t, r) {
        (null == r || r > t.length) && (r = t.length);
        for (var e = 0, n = new Array(r); e < r; e++) n[e] = t[e];
        return n;
      }
      var o = e(1),
        s = e(0).isFunction;
      t.exports = function (t, r) {
        if (void 0 !== r)
          return Array.isArray(this.items)
            ? this.items.filter(function (e) {
                return void 0 !== e[t] && e[t] === r;
              }).length > 0
            : void 0 !== this.items[t] && this.items[t] === r;
        if (s(t))
          return (
            this.items.filter(function (r, e) {
              return t(r, e);
            }).length > 0
          );
        if (Array.isArray(this.items)) return -1 !== this.items.indexOf(t);
        var e = o(this.items);
        return e.push.apply(e, n(Object.keys(this.items))), -1 !== e.indexOf(t);
      };
    },
    function (t, r, e) {
      "use strict";
      var n = e(3);
      t.exports = function (t) {
        for (
          var r = arguments.length, e = new Array(r > 1 ? r - 1 : 0), i = 1;
          i < r;
          i++
        )
          e[i - 1] = arguments[i];
        n(e).forEach(function (r) {
          delete t[r];
        });
      };
    },
    function (t, r, e) {
      "use strict";
      t.exports = function (t, r) {
        if (Array.isArray(this.items) && this.items.length) return t(this);
        if (Object.keys(this.items).length) return t(this);
        if (void 0 !== r) {
          if (Array.isArray(this.items) && !this.items.length) return r(this);
          if (!Object.keys(this.items).length) return r(this);
        }
        return this;
      };
    },
    function (t, r, e) {
      "use strict";
      t.exports = function (t, r) {
        if (Array.isArray(this.items) && !this.items.length) return t(this);
        if (!Object.keys(this.items).length) return t(this);
        if (void 0 !== r) {
          if (Array.isArray(this.items) && this.items.length) return r(this);
          if (Object.keys(this.items).length) return r(this);
        }
        return this;
      };
    },
    function (t, r, e) {
      "use strict";
      function n(t) {
        return (n =
          "function" == typeof Symbol && "symbol" == typeof Symbol.iterator
            ? function (t) {
                return typeof t;
              }
            : function (t) {
                return t &&
                  "function" == typeof Symbol &&
                  t.constructor === Symbol &&
                  t !== Symbol.prototype
                  ? "symbol"
                  : typeof t;
              })(t);
      }
      function i(t) {
        void 0 === t || Array.isArray(t) || "object" === n(t)
          ? t instanceof this.constructor
            ? (this.items = t.all())
            : (this.items = t || [])
          : (this.items = [t]);
      }
      var o = e(11);
      "undefined" != typeof Symbol && (i.prototype[Symbol.iterator] = o),
        (i.prototype.toJSON = function () {
          return this.items;
        }),
        (i.prototype.all = e(12)),
        (i.prototype.average = e(4)),
        (i.prototype.avg = e(13)),
        (i.prototype.chunk = e(14)),
        (i.prototype.collapse = e(15)),
        (i.prototype.combine = e(16)),
        (i.prototype.concat = e(17)),
        (i.prototype.contains = e(6)),
        (i.prototype.containsOneItem = e(18)),
        (i.prototype.count = e(19)),
        (i.prototype.countBy = e(20)),
        (i.prototype.crossJoin = e(21)),
        (i.prototype.dd = e(22)),
        (i.prototype.diff = e(24)),
        (i.prototype.diffAssoc = e(25)),
        (i.prototype.diffKeys = e(26)),
        (i.prototype.doesntContain = e(27)),
        (i.prototype.dump = e(28)),
        (i.prototype.duplicates = e(29)),
        (i.prototype.each = e(30)),
        (i.prototype.eachSpread = e(31)),
        (i.prototype.every = e(32)),
        (i.prototype.except = e(33)),
        (i.prototype.filter = e(34)),
        (i.prototype.first = e(35)),
        (i.prototype.firstOrFail = e(36)),
        (i.prototype.firstWhere = e(37)),
        (i.prototype.flatMap = e(38)),
        (i.prototype.flatten = e(39)),
        (i.prototype.flip = e(40)),
        (i.prototype.forPage = e(41)),
        (i.prototype.forget = e(42)),
        (i.prototype.get = e(43)),
        (i.prototype.groupBy = e(44)),
        (i.prototype.has = e(45)),
        (i.prototype.implode = e(46)),
        (i.prototype.intersect = e(47)),
        (i.prototype.intersectByKeys = e(48)),
        (i.prototype.isEmpty = e(49)),
        (i.prototype.isNotEmpty = e(50)),
        (i.prototype.join = e(51)),
        (i.prototype.keyBy = e(52)),
        (i.prototype.keys = e(53)),
        (i.prototype.last = e(54)),
        (i.prototype.macro = e(55)),
        (i.prototype.make = e(56)),
        (i.prototype.map = e(57)),
        (i.prototype.mapSpread = e(58)),
        (i.prototype.mapToDictionary = e(59)),
        (i.prototype.mapInto = e(60)),
        (i.prototype.mapToGroups = e(61)),
        (i.prototype.mapWithKeys = e(62)),
        (i.prototype.max = e(63)),
        (i.prototype.median = e(64)),
        (i.prototype.merge = e(65)),
        (i.prototype.mergeRecursive = e(66)),
        (i.prototype.min = e(67)),
        (i.prototype.mode = e(68)),
        (i.prototype.nth = e(69)),
        (i.prototype.only = e(70)),
        (i.prototype.pad = e(71)),
        (i.prototype.partition = e(72)),
        (i.prototype.pipe = e(73)),
        (i.prototype.pluck = e(74)),
        (i.prototype.pop = e(75)),
        (i.prototype.prepend = e(76)),
        (i.prototype.pull = e(77)),
        (i.prototype.push = e(78)),
        (i.prototype.put = e(79)),
        (i.prototype.random = e(80)),
        (i.prototype.reduce = e(81)),
        (i.prototype.reject = e(82)),
        (i.prototype.replace = e(83)),
        (i.prototype.replaceRecursive = e(84)),
        (i.prototype.reverse = e(85)),
        (i.prototype.search = e(86)),
        (i.prototype.shift = e(87)),
        (i.prototype.shuffle = e(88)),
        (i.prototype.skip = e(89)),
        (i.prototype.skipUntil = e(90)),
        (i.prototype.skipWhile = e(91)),
        (i.prototype.slice = e(92)),
        (i.prototype.sole = e(93)),
        (i.prototype.some = e(94)),
        (i.prototype.sort = e(95)),
        (i.prototype.sortDesc = e(96)),
        (i.prototype.sortBy = e(97)),
        (i.prototype.sortByDesc = e(98)),
        (i.prototype.sortKeys = e(99)),
        (i.prototype.sortKeysDesc = e(100)),
        (i.prototype.splice = e(101)),
        (i.prototype.split = e(102)),
        (i.prototype.sum = e(103)),
        (i.prototype.take = e(104)),
        (i.prototype.takeUntil = e(105)),
        (i.prototype.takeWhile = e(106)),
        (i.prototype.tap = e(107)),
        (i.prototype.times = e(108)),
        (i.prototype.toArray = e(109)),
        (i.prototype.toJson = e(110)),
        (i.prototype.transform = e(111)),
        (i.prototype.undot = e(112)),
        (i.prototype.unless = e(113)),
        (i.prototype.unlessEmpty = e(8)),
        (i.prototype.unlessNotEmpty = e(9)),
        (i.prototype.union = e(114)),
        (i.prototype.unique = e(115)),
        (i.prototype.unwrap = e(116)),
        (i.prototype.values = e(117)),
        (i.prototype.when = e(118)),
        (i.prototype.whenEmpty = e(9)),
        (i.prototype.whenNotEmpty = e(8)),
        (i.prototype.where = e(119)),
        (i.prototype.whereBetween = e(120)),
        (i.prototype.whereIn = e(121)),
        (i.prototype.whereInstanceOf = e(122)),
        (i.prototype.whereNotBetween = e(123)),
        (i.prototype.whereNotIn = e(124)),
        (i.prototype.whereNull = e(125)),
        (i.prototype.whereNotNull = e(126)),
        (i.prototype.wrap = e(127)),
        (i.prototype.zip = e(128));
      var s = function (t) {
        return new i(t);
      };
      (t.exports = s),
        (t.exports.collect = s),
        (t.exports.default = s),
        (t.exports.Collection = i);
    },
    function (t, r, e) {
      "use strict";
      t.exports = function () {
        var t = this,
          r = -1;
        return {
          next: function () {
            return (r += 1), { value: t.items[r], done: r >= t.items.length };
          },
        };
      };
    },
    function (t, r, e) {
      "use strict";
      t.exports = function () {
        return this.items;
      };
    },
    function (t, r, e) {
      "use strict";
      var n = e(4);
      t.exports = n;
    },
    function (t, r, e) {
      "use strict";
      function n(t) {
        return (n =
          "function" == typeof Symbol && "symbol" == typeof Symbol.iterator
            ? function (t) {
                return typeof t;
              }
            : function (t) {
                return t &&
                  "function" == typeof Symbol &&
                  t.constructor === Symbol &&
                  t !== Symbol.prototype
                  ? "symbol"
                  : typeof t;
              })(t);
      }
      t.exports = function (t) {
        var r = this,
          e = [],
          i = 0;
        if (Array.isArray(this.items))
          do {
            var o = this.items.slice(i, i + t),
              s = new this.constructor(o);
            e.push(s), (i += t);
          } while (i < this.items.length);
        else if ("object" === n(this.items)) {
          var u = Object.keys(this.items),
            c = function () {
              var n = u.slice(i, i + t),
                o = new r.constructor({});
              n.forEach(function (t) {
                return o.put(t, r.items[t]);
              }),
                e.push(o),
                (i += t);
            };
          do {
            c();
          } while (i < u.length);
        } else e.push(new this.constructor([this.items]));
        return new this.constructor(e);
      };
    },
    function (t, r, e) {
      "use strict";
      function n(t) {
        return (
          (function (t) {
            if (Array.isArray(t)) return i(t);
          })(t) ||
          (function (t) {
            if (
              ("undefined" != typeof Symbol && null != t[Symbol.iterator]) ||
              null != t["@@iterator"]
            )
              return Array.from(t);
          })(t) ||
          (function (t, r) {
            if (!t) return;
            if ("string" == typeof t) return i(t, r);
            var e = Object.prototype.toString.call(t).slice(8, -1);
            "Object" === e && t.constructor && (e = t.constructor.name);
            if ("Map" === e || "Set" === e) return Array.from(t);
            if (
              "Arguments" === e ||
              /^(?:Ui|I)nt(?:8|16|32)(?:Clamped)?Array$/.test(e)
            )
              return i(t, r);
          })(t) ||
          (function () {
            throw new TypeError(
              "Invalid attempt to spread non-iterable instance.\nIn order to be iterable, non-array objects must have a [Symbol.iterator]() method."
            );
          })()
        );
      }
      function i(t, r) {
        (null == r || r > t.length) && (r = t.length);
        for (var e = 0, n = new Array(r); e < r; e++) n[e] = t[e];
        return n;
      }
      t.exports = function () {
        var t;
        return new this.constructor((t = []).concat.apply(t, n(this.items)));
      };
    },
    function (t, r, e) {
      "use strict";
      function n(t, r) {
        return (
          (function (t) {
            if (Array.isArray(t)) return t;
          })(t) ||
          (function (t, r) {
            var e =
              null == t
                ? null
                : ("undefined" != typeof Symbol && t[Symbol.iterator]) ||
                  t["@@iterator"];
            if (null == e) return;
            var n,
              i,
              o = [],
              s = !0,
              u = !1;
            try {
              for (
                e = e.call(t);
                !(s = (n = e.next()).done) &&
                (o.push(n.value), !r || o.length !== r);
                s = !0
              );
            } catch (t) {
              (u = !0), (i = t);
            } finally {
              try {
                s || null == e.return || e.return();
              } finally {
                if (u) throw i;
              }
            }
            return o;
          })(t, r) ||
          (function (t, r) {
            if (!t) return;
            if ("string" == typeof t) return i(t, r);
            var e = Object.prototype.toString.call(t).slice(8, -1);
            "Object" === e && t.constructor && (e = t.constructor.name);
            if ("Map" === e || "Set" === e) return Array.from(t);
            if (
              "Arguments" === e ||
              /^(?:Ui|I)nt(?:8|16|32)(?:Clamped)?Array$/.test(e)
            )
              return i(t, r);
          })(t, r) ||
          (function () {
            throw new TypeError(
              "Invalid attempt to destructure non-iterable instance.\nIn order to be iterable, non-array objects must have a [Symbol.iterator]() method."
            );
          })()
        );
      }
      function i(t, r) {
        (null == r || r > t.length) && (r = t.length);
        for (var e = 0, n = new Array(r); e < r; e++) n[e] = t[e];
        return n;
      }
      function o(t) {
        return (o =
          "function" == typeof Symbol && "symbol" == typeof Symbol.iterator
            ? function (t) {
                return typeof t;
              }
            : function (t) {
                return t &&
                  "function" == typeof Symbol &&
                  t.constructor === Symbol &&
                  t !== Symbol.prototype
                  ? "symbol"
                  : typeof t;
              })(t);
      }
      t.exports = function (t) {
        var r = this,
          e = t;
        e instanceof this.constructor && (e = t.all());
        var i = {};
        if (Array.isArray(this.items) && Array.isArray(e))
          this.items.forEach(function (t, r) {
            i[t] = e[r];
          });
        else if ("object" === o(this.items) && "object" === o(e))
          Object.keys(this.items).forEach(function (t, n) {
            i[r.items[t]] = e[Object.keys(e)[n]];
          });
        else if (Array.isArray(this.items)) i[this.items[0]] = e;
        else if ("string" == typeof this.items && Array.isArray(e)) {
          var s = n(e, 1);
          i[this.items] = s[0];
        } else "string" == typeof this.items && (i[this.items] = e);
        return new this.constructor(i);
      };
    },
    function (t, r, e) {
      "use strict";
      function n(t) {
        return (n =
          "function" == typeof Symbol && "symbol" == typeof Symbol.iterator
            ? function (t) {
                return typeof t;
              }
            : function (t) {
                return t &&
                  "function" == typeof Symbol &&
                  t.constructor === Symbol &&
                  t !== Symbol.prototype
                  ? "symbol"
                  : typeof t;
              })(t);
      }
      var i = e(5);
      t.exports = function (t) {
        var r = t;
        t instanceof this.constructor
          ? (r = t.all())
          : "object" === n(t) &&
            ((r = []),
            Object.keys(t).forEach(function (e) {
              r.push(t[e]);
            }));
        var e = i(this.items);
        return (
          r.forEach(function (t) {
            "object" === n(t)
              ? Object.keys(t).forEach(function (r) {
                  return e.push(t[r]);
                })
              : e.push(t);
          }),
          new this.constructor(e)
        );
      };
    },
    function (t, r, e) {
      "use strict";
      t.exports = function () {
        return 1 === this.count();
      };
    },
    function (t, r, e) {
      "use strict";
      t.exports = function () {
        var t = 0;
        return (
          Array.isArray(this.items) && (t = this.items.length),
          Math.max(Object.keys(this.items).length, t)
        );
      };
    },
    function (t, r, e) {
      "use strict";
      t.exports = function () {
        var t =
          arguments.length > 0 && void 0 !== arguments[0]
            ? arguments[0]
            : function (t) {
                return t;
              };
        return new this.constructor(this.items).groupBy(t).map(function (t) {
          return t.count();
        });
      };
    },
    function (t, r, e) {
      "use strict";
      t.exports = function () {
        function t(r, e, n) {
          var i = n[0];
          i instanceof e && (i = i.all());
          for (
            var o = n.slice(1), s = !o.length, u = [], c = 0;
            c < i.length;
            c += 1
          ) {
            var f = r.slice();
            f.push(i[c]), s ? u.push(f) : (u = u.concat(t(f, e, o)));
          }
          return u;
        }
        for (var r = arguments.length, e = new Array(r), n = 0; n < r; n++)
          e[n] = arguments[n];
        return new this.constructor(
          t([], this.constructor, [].concat([this.items], e))
        );
      };
    },
    function (t, r, e) {
      "use strict";
      (function (r) {
        t.exports = function () {
          this.dump(), void 0 !== r && r.exit(1);
        };
      }.call(this, e(23)));
    },
    function (t, r) {
      var e,
        n,
        i = (t.exports = {});
      function o() {
        throw new Error("setTimeout has not been defined");
      }
      function s() {
        throw new Error("clearTimeout has not been defined");
      }
      function u(t) {
        if (e === setTimeout) return setTimeout(t, 0);
        if ((e === o || !e) && setTimeout)
          return (e = setTimeout), setTimeout(t, 0);
        try {
          return e(t, 0);
        } catch (r) {
          try {
            return e.call(null, t, 0);
          } catch (r) {
            return e.call(this, t, 0);
          }
        }
      }
      !(function () {
        try {
          e = "function" == typeof setTimeout ? setTimeout : o;
        } catch (t) {
          e = o;
        }
        try {
          n = "function" == typeof clearTimeout ? clearTimeout : s;
        } catch (t) {
          n = s;
        }
      })();
      var c,
        f = [],
        a = !1,
        p = -1;
      function l() {
        a &&
          c &&
          ((a = !1), c.length ? (f = c.concat(f)) : (p = -1), f.length && h());
      }
      function h() {
        if (!a) {
          var t = u(l);
          a = !0;
          for (var r = f.length; r; ) {
            for (c = f, f = []; ++p < r; ) c && c[p].run();
            (p = -1), (r = f.length);
          }
          (c = null),
            (a = !1),
            (function (t) {
              if (n === clearTimeout) return clearTimeout(t);
              if ((n === s || !n) && clearTimeout)
                return (n = clearTimeout), clearTimeout(t);
              try {
                n(t);
              } catch (r) {
                try {
                  return n.call(null, t);
                } catch (r) {
                  return n.call(this, t);
                }
              }
            })(t);
        }
      }
      function y(t, r) {
        (this.fun = t), (this.array = r);
      }
      function m() {}
      (i.nextTick = function (t) {
        var r = new Array(arguments.length - 1);
        if (arguments.length > 1)
          for (var e = 1; e < arguments.length; e++) r[e - 1] = arguments[e];
        f.push(new y(t, r)), 1 !== f.length || a || u(h);
      }),
        (y.prototype.run = function () {
          this.fun.apply(null, this.array);
        }),
        (i.title = "browser"),
        (i.browser = !0),
        (i.env = {}),
        (i.argv = []),
        (i.version = ""),
        (i.versions = {}),
        (i.on = m),
        (i.addListener = m),
        (i.once = m),
        (i.off = m),
        (i.removeListener = m),
        (i.removeAllListeners = m),
        (i.emit = m),
        (i.prependListener = m),
        (i.prependOnceListener = m),
        (i.listeners = function (t) {
          return [];
        }),
        (i.binding = function (t) {
          throw new Error("process.binding is not supported");
        }),
        (i.cwd = function () {
          return "/";
        }),
        (i.chdir = function (t) {
          throw new Error("process.chdir is not supported");
        }),
        (i.umask = function () {
          return 0;
        });
    },
    function (t, r, e) {
      "use strict";
      t.exports = function (t) {
        var r;
        r = t instanceof this.constructor ? t.all() : t;
        var e = this.items.filter(function (t) {
          return -1 === r.indexOf(t);
        });
        return new this.constructor(e);
      };
    },
    function (t, r, e) {
      "use strict";
      t.exports = function (t) {
        var r = this,
          e = t;
        t instanceof this.constructor && (e = t.all());
        var n = {};
        return (
          Object.keys(this.items).forEach(function (t) {
            (void 0 !== e[t] && e[t] === r.items[t]) || (n[t] = r.items[t]);
          }),
          new this.constructor(n)
        );
      };
    },
    function (t, r, e) {
      "use strict";
      t.exports = function (t) {
        var r;
        r = t instanceof this.constructor ? t.all() : t;
        var e = Object.keys(r),
          n = Object.keys(this.items).filter(function (t) {
            return -1 === e.indexOf(t);
          });
        return new this.constructor(this.items).only(n);
      };
    },
    function (t, r, e) {
      "use strict";
      t.exports = function (t, r) {
        return !this.contains(t, r);
      };
    },
    function (t, r, e) {
      "use strict";
      t.exports = function () {
        return console.log(this), this;
      };
    },
    function (t, r, e) {
      "use strict";
      function n(t) {
        return (n =
          "function" == typeof Symbol && "symbol" == typeof Symbol.iterator
            ? function (t) {
                return typeof t;
              }
            : function (t) {
                return t &&
                  "function" == typeof Symbol &&
                  t.constructor === Symbol &&
                  t !== Symbol.prototype
                  ? "symbol"
                  : typeof t;
              })(t);
      }
      t.exports = function () {
        var t = this,
          r = [],
          e = {},
          i = function (t) {
            return Array.isArray(t) || "object" === n(t)
              ? JSON.stringify(t)
              : t;
          };
        return (
          Array.isArray(this.items)
            ? this.items.forEach(function (t, n) {
                var o = i(t);
                -1 === r.indexOf(o) ? r.push(o) : (e[n] = t);
              })
            : "object" === n(this.items) &&
              Object.keys(this.items).forEach(function (n) {
                var o = i(t.items[n]);
                -1 === r.indexOf(o) ? r.push(o) : (e[n] = t.items[n]);
              }),
          new this.constructor(e)
        );
      };
    },
    function (t, r, e) {
      "use strict";
      t.exports = function (t) {
        var r = !1;
        if (Array.isArray(this.items))
          for (var e = this.items.length, n = 0; n < e && !r; n += 1)
            r = !1 === t(this.items[n], n, this.items);
        else
          for (
            var i = Object.keys(this.items), o = i.length, s = 0;
            s < o && !r;
            s += 1
          ) {
            var u = i[s];
            r = !1 === t(this.items[u], u, this.items);
          }
        return this;
      };
    },
    function (t, r, e) {
      "use strict";
      function n(t) {
        return (
          (function (t) {
            if (Array.isArray(t)) return i(t);
          })(t) ||
          (function (t) {
            if (
              ("undefined" != typeof Symbol && null != t[Symbol.iterator]) ||
              null != t["@@iterator"]
            )
              return Array.from(t);
          })(t) ||
          (function (t, r) {
            if (!t) return;
            if ("string" == typeof t) return i(t, r);
            var e = Object.prototype.toString.call(t).slice(8, -1);
            "Object" === e && t.constructor && (e = t.constructor.name);
            if ("Map" === e || "Set" === e) return Array.from(t);
            if (
              "Arguments" === e ||
              /^(?:Ui|I)nt(?:8|16|32)(?:Clamped)?Array$/.test(e)
            )
              return i(t, r);
          })(t) ||
          (function () {
            throw new TypeError(
              "Invalid attempt to spread non-iterable instance.\nIn order to be iterable, non-array objects must have a [Symbol.iterator]() method."
            );
          })()
        );
      }
      function i(t, r) {
        (null == r || r > t.length) && (r = t.length);
        for (var e = 0, n = new Array(r); e < r; e++) n[e] = t[e];
        return n;
      }
      t.exports = function (t) {
        return (
          this.each(function (r, e) {
            t.apply(void 0, n(r).concat([e]));
          }),
          this
        );
      };
    },
    function (t, r, e) {
      "use strict";
      var n = e(1);
      t.exports = function (t) {
        return n(this.items).every(t);
      };
    },
    function (t, r, e) {
      "use strict";
      var n = e(3);
      t.exports = function () {
        for (
          var t = this, r = arguments.length, e = new Array(r), i = 0;
          i < r;
          i++
        )
          e[i] = arguments[i];
        var o = n(e);
        if (Array.isArray(this.items)) {
          var s = this.items.filter(function (t) {
            return -1 === o.indexOf(t);
          });
          return new this.constructor(s);
        }
        var u = {};
        return (
          Object.keys(this.items).forEach(function (r) {
            -1 === o.indexOf(r) && (u[r] = t.items[r]);
          }),
          new this.constructor(u)
        );
      };
    },
    function (t, r, e) {
      "use strict";
      function n(t) {
        return (n =
          "function" == typeof Symbol && "symbol" == typeof Symbol.iterator
            ? function (t) {
                return typeof t;
              }
            : function (t) {
                return t &&
                  "function" == typeof Symbol &&
                  t.constructor === Symbol &&
                  t !== Symbol.prototype
                  ? "symbol"
                  : typeof t;
              })(t);
      }
      function i(t) {
        if (Array.isArray(t)) {
          if (t.length) return !1;
        } else if (null != t && "object" === n(t)) {
          if (Object.keys(t).length) return !1;
        } else if (t) return !1;
        return !0;
      }
      t.exports = function (t) {
        var r = t || !1,
          e = null;
        return (
          (e = Array.isArray(this.items)
            ? (function (t, r) {
                if (t) return r.filter(t);
                for (var e = [], n = 0; n < r.length; n += 1) {
                  var o = r[n];
                  i(o) || e.push(o);
                }
                return e;
              })(r, this.items)
            : (function (t, r) {
                var e = {};
                return (
                  Object.keys(r).forEach(function (n) {
                    t ? t(r[n], n) && (e[n] = r[n]) : i(r[n]) || (e[n] = r[n]);
                  }),
                  e
                );
              })(r, this.items)),
          new this.constructor(e)
        );
      };
    },
    function (t, r, e) {
      "use strict";
      var n = e(0).isFunction;
      t.exports = function (t, r) {
        if (n(t)) {
          for (var e = Object.keys(this.items), i = 0; i < e.length; i += 1) {
            var o = e[i],
              s = this.items[o];
            if (t(s, o)) return s;
          }
          return n(r) ? r() : r;
        }
        if (
          (Array.isArray(this.items) && this.items.length) ||
          Object.keys(this.items).length
        ) {
          if (Array.isArray(this.items)) return this.items[0];
          var u = Object.keys(this.items)[0];
          return this.items[u];
        }
        return n(r) ? r() : r;
      };
    },
    function (t, r, e) {
      "use strict";
      var n = e(0).isFunction;
      t.exports = function (t, r, e) {
        if (n(t))
          return this.first(t, function () {
            throw new Error("Item not found.");
          });
        var i = this.where(t, r, e);
        if (i.isEmpty()) throw new Error("Item not found.");
        return i.first();
      };
    },
    function (t, r, e) {
      "use strict";
      t.exports = function (t, r, e) {
        return this.where(t, r, e).first() || null;
      };
    },
    function (t, r, e) {
      "use strict";
      t.exports = function (t) {
        return this.map(t).collapse();
      };
    },
    function (t, r, e) {
      "use strict";
      var n = e(0),
        i = n.isArray,
        o = n.isObject;
      t.exports = function (t) {
        var r = t || 1 / 0,
          e = !1,
          n = [],
          s = function (t) {
            (n = []),
              i(t)
                ? t.forEach(function (t) {
                    i(t)
                      ? (n = n.concat(t))
                      : o(t)
                      ? Object.keys(t).forEach(function (r) {
                          n = n.concat(t[r]);
                        })
                      : n.push(t);
                  })
                : Object.keys(t).forEach(function (r) {
                    i(t[r])
                      ? (n = n.concat(t[r]))
                      : o(t[r])
                      ? Object.keys(t[r]).forEach(function (e) {
                          n = n.concat(t[r][e]);
                        })
                      : n.push(t[r]);
                  }),
              (e =
                0 ===
                (e = n.filter(function (t) {
                  return o(t);
                })).length),
              (r -= 1);
          };
        for (s(this.items); !e && r > 0; ) s(n);
        return new this.constructor(n);
      };
    },
    function (t, r, e) {
      "use strict";
      t.exports = function () {
        var t = this,
          r = {};
        return (
          Array.isArray(this.items)
            ? Object.keys(this.items).forEach(function (e) {
                r[t.items[e]] = Number(e);
              })
            : Object.keys(this.items).forEach(function (e) {
                r[t.items[e]] = e;
              }),
          new this.constructor(r)
        );
      };
    },
    function (t, r, e) {
      "use strict";
      t.exports = function (t, r) {
        var e = this,
          n = {};
        return (
          Array.isArray(this.items)
            ? (n = this.items.slice(t * r - r, t * r))
            : Object.keys(this.items)
                .slice(t * r - r, t * r)
                .forEach(function (t) {
                  n[t] = e.items[t];
                }),
          new this.constructor(n)
        );
      };
    },
    function (t, r, e) {
      "use strict";
      t.exports = function (t) {
        return (
          Array.isArray(this.items)
            ? this.items.splice(t, 1)
            : delete this.items[t],
          this
        );
      };
    },
    function (t, r, e) {
      "use strict";
      var n = e(0).isFunction;
      t.exports = function (t) {
        var r =
          arguments.length > 1 && void 0 !== arguments[1] ? arguments[1] : null;
        return void 0 !== this.items[t]
          ? this.items[t]
          : n(r)
          ? r()
          : null !== r
          ? r
          : null;
      };
    },
    function (t, r, e) {
      "use strict";
      var n = e(2),
        i = e(0).isFunction;
      t.exports = function (t) {
        var r = this,
          e = {};
        return (
          this.items.forEach(function (o, s) {
            var u;
            (u = i(t) ? t(o, s) : n(o, t) || 0 === n(o, t) ? n(o, t) : ""),
              void 0 === e[u] && (e[u] = new r.constructor([])),
              e[u].push(o);
          }),
          new this.constructor(e)
        );
      };
    },
    function (t, r, e) {
      "use strict";
      var n = e(3);
      t.exports = function () {
        for (
          var t = this, r = arguments.length, e = new Array(r), i = 0;
          i < r;
          i++
        )
          e[i] = arguments[i];
        var o = n(e);
        return (
          o.filter(function (r) {
            return Object.hasOwnProperty.call(t.items, r);
          }).length === o.length
        );
      };
    },
    function (t, r, e) {
      "use strict";
      t.exports = function (t, r) {
        return void 0 === r
          ? this.items.join(t)
          : new this.constructor(this.items).pluck(t).all().join(r);
      };
    },
    function (t, r, e) {
      "use strict";
      t.exports = function (t) {
        var r = t;
        t instanceof this.constructor && (r = t.all());
        var e = this.items.filter(function (t) {
          return -1 !== r.indexOf(t);
        });
        return new this.constructor(e);
      };
    },
    function (t, r, e) {
      "use strict";
      t.exports = function (t) {
        var r = this,
          e = Object.keys(t);
        t instanceof this.constructor && (e = Object.keys(t.all()));
        var n = {};
        return (
          Object.keys(this.items).forEach(function (t) {
            -1 !== e.indexOf(t) && (n[t] = r.items[t]);
          }),
          new this.constructor(n)
        );
      };
    },
    function (t, r, e) {
      "use strict";
      t.exports = function () {
        return Array.isArray(this.items)
          ? !this.items.length
          : !Object.keys(this.items).length;
      };
    },
    function (t, r, e) {
      "use strict";
      t.exports = function () {
        return !this.isEmpty();
      };
    },
    function (t, r, e) {
      "use strict";
      t.exports = function (t, r) {
        var e = this.values();
        if (void 0 === r) return e.implode(t);
        var n = e.count();
        if (0 === n) return "";
        if (1 === n) return e.last();
        var i = e.pop();
        return e.implode(t) + r + i;
      };
    },
    function (t, r, e) {
      "use strict";
      var n = e(2),
        i = e(0).isFunction;
      t.exports = function (t) {
        var r = {};
        return (
          i(t)
            ? this.items.forEach(function (e) {
                r[t(e)] = e;
              })
            : this.items.forEach(function (e) {
                var i = n(e, t);
                r[i || ""] = e;
              }),
          new this.constructor(r)
        );
      };
    },
    function (t, r, e) {
      "use strict";
      t.exports = function () {
        var t = Object.keys(this.items);
        return (
          Array.isArray(this.items) && (t = t.map(Number)),
          new this.constructor(t)
        );
      };
    },
    function (t, r, e) {
      "use strict";
      var n = e(0).isFunction;
      t.exports = function (t, r) {
        var e = this.items;
        if (
          (n(t) && (e = this.filter(t).all()),
          (Array.isArray(e) && !e.length) || !Object.keys(e).length)
        )
          return n(r) ? r() : r;
        if (Array.isArray(e)) return e[e.length - 1];
        var i = Object.keys(e);
        return e[i[i.length - 1]];
      };
    },
    function (t, r, e) {
      "use strict";
      t.exports = function (t, r) {
        this.constructor.prototype[t] = r;
      };
    },
    function (t, r, e) {
      "use strict";
      t.exports = function () {
        var t =
          arguments.length > 0 && void 0 !== arguments[0] ? arguments[0] : [];
        return new this.constructor(t);
      };
    },
    function (t, r, e) {
      "use strict";
      t.exports = function (t) {
        var r = this;
        if (Array.isArray(this.items))
          return new this.constructor(this.items.map(t));
        var e = {};
        return (
          Object.keys(this.items).forEach(function (n) {
            e[n] = t(r.items[n], n);
          }),
          new this.constructor(e)
        );
      };
    },
    function (t, r, e) {
      "use strict";
      function n(t) {
        return (
          (function (t) {
            if (Array.isArray(t)) return i(t);
          })(t) ||
          (function (t) {
            if (
              ("undefined" != typeof Symbol && null != t[Symbol.iterator]) ||
              null != t["@@iterator"]
            )
              return Array.from(t);
          })(t) ||
          (function (t, r) {
            if (!t) return;
            if ("string" == typeof t) return i(t, r);
            var e = Object.prototype.toString.call(t).slice(8, -1);
            "Object" === e && t.constructor && (e = t.constructor.name);
            if ("Map" === e || "Set" === e) return Array.from(t);
            if (
              "Arguments" === e ||
              /^(?:Ui|I)nt(?:8|16|32)(?:Clamped)?Array$/.test(e)
            )
              return i(t, r);
          })(t) ||
          (function () {
            throw new TypeError(
              "Invalid attempt to spread non-iterable instance.\nIn order to be iterable, non-array objects must have a [Symbol.iterator]() method."
            );
          })()
        );
      }
      function i(t, r) {
        (null == r || r > t.length) && (r = t.length);
        for (var e = 0, n = new Array(r); e < r; e++) n[e] = t[e];
        return n;
      }
      t.exports = function (t) {
        return this.map(function (r, e) {
          return t.apply(void 0, n(r).concat([e]));
        });
      };
    },
    function (t, r, e) {
      "use strict";
      function n(t, r) {
        return (
          (function (t) {
            if (Array.isArray(t)) return t;
          })(t) ||
          (function (t, r) {
            var e =
              null == t
                ? null
                : ("undefined" != typeof Symbol && t[Symbol.iterator]) ||
                  t["@@iterator"];
            if (null == e) return;
            var n,
              i,
              o = [],
              s = !0,
              u = !1;
            try {
              for (
                e = e.call(t);
                !(s = (n = e.next()).done) &&
                (o.push(n.value), !r || o.length !== r);
                s = !0
              );
            } catch (t) {
              (u = !0), (i = t);
            } finally {
              try {
                s || null == e.return || e.return();
              } finally {
                if (u) throw i;
              }
            }
            return o;
          })(t, r) ||
          (function (t, r) {
            if (!t) return;
            if ("string" == typeof t) return i(t, r);
            var e = Object.prototype.toString.call(t).slice(8, -1);
            "Object" === e && t.constructor && (e = t.constructor.name);
            if ("Map" === e || "Set" === e) return Array.from(t);
            if (
              "Arguments" === e ||
              /^(?:Ui|I)nt(?:8|16|32)(?:Clamped)?Array$/.test(e)
            )
              return i(t, r);
          })(t, r) ||
          (function () {
            throw new TypeError(
              "Invalid attempt to destructure non-iterable instance.\nIn order to be iterable, non-array objects must have a [Symbol.iterator]() method."
            );
          })()
        );
      }
      function i(t, r) {
        (null == r || r > t.length) && (r = t.length);
        for (var e = 0, n = new Array(r); e < r; e++) n[e] = t[e];
        return n;
      }
      t.exports = function (t) {
        var r = {};
        return (
          this.items.forEach(function (e, i) {
            var o = n(t(e, i), 2),
              s = o[0],
              u = o[1];
            void 0 === r[s] ? (r[s] = [u]) : r[s].push(u);
          }),
          new this.constructor(r)
        );
      };
    },
    function (t, r, e) {
      "use strict";
      t.exports = function (t) {
        return this.map(function (r, e) {
          return new t(r, e);
        });
      };
    },
    function (t, r, e) {
      "use strict";
      function n(t, r) {
        return (
          (function (t) {
            if (Array.isArray(t)) return t;
          })(t) ||
          (function (t, r) {
            var e =
              null == t
                ? null
                : ("undefined" != typeof Symbol && t[Symbol.iterator]) ||
                  t["@@iterator"];
            if (null == e) return;
            var n,
              i,
              o = [],
              s = !0,
              u = !1;
            try {
              for (
                e = e.call(t);
                !(s = (n = e.next()).done) &&
                (o.push(n.value), !r || o.length !== r);
                s = !0
              );
            } catch (t) {
              (u = !0), (i = t);
            } finally {
              try {
                s || null == e.return || e.return();
              } finally {
                if (u) throw i;
              }
            }
            return o;
          })(t, r) ||
          (function (t, r) {
            if (!t) return;
            if ("string" == typeof t) return i(t, r);
            var e = Object.prototype.toString.call(t).slice(8, -1);
            "Object" === e && t.constructor && (e = t.constructor.name);
            if ("Map" === e || "Set" === e) return Array.from(t);
            if (
              "Arguments" === e ||
              /^(?:Ui|I)nt(?:8|16|32)(?:Clamped)?Array$/.test(e)
            )
              return i(t, r);
          })(t, r) ||
          (function () {
            throw new TypeError(
              "Invalid attempt to destructure non-iterable instance.\nIn order to be iterable, non-array objects must have a [Symbol.iterator]() method."
            );
          })()
        );
      }
      function i(t, r) {
        (null == r || r > t.length) && (r = t.length);
        for (var e = 0, n = new Array(r); e < r; e++) n[e] = t[e];
        return n;
      }
      t.exports = function (t) {
        var r = {};
        return (
          this.items.forEach(function (e, i) {
            var o = n(t(e, i), 2),
              s = o[0],
              u = o[1];
            void 0 === r[s] ? (r[s] = [u]) : r[s].push(u);
          }),
          new this.constructor(r)
        );
      };
    },
    function (t, r, e) {
      "use strict";
      function n(t, r) {
        return (
          (function (t) {
            if (Array.isArray(t)) return t;
          })(t) ||
          (function (t, r) {
            var e =
              null == t
                ? null
                : ("undefined" != typeof Symbol && t[Symbol.iterator]) ||
                  t["@@iterator"];
            if (null == e) return;
            var n,
              i,
              o = [],
              s = !0,
              u = !1;
            try {
              for (
                e = e.call(t);
                !(s = (n = e.next()).done) &&
                (o.push(n.value), !r || o.length !== r);
                s = !0
              );
            } catch (t) {
              (u = !0), (i = t);
            } finally {
              try {
                s || null == e.return || e.return();
              } finally {
                if (u) throw i;
              }
            }
            return o;
          })(t, r) ||
          (function (t, r) {
            if (!t) return;
            if ("string" == typeof t) return i(t, r);
            var e = Object.prototype.toString.call(t).slice(8, -1);
            "Object" === e && t.constructor && (e = t.constructor.name);
            if ("Map" === e || "Set" === e) return Array.from(t);
            if (
              "Arguments" === e ||
              /^(?:Ui|I)nt(?:8|16|32)(?:Clamped)?Array$/.test(e)
            )
              return i(t, r);
          })(t, r) ||
          (function () {
            throw new TypeError(
              "Invalid attempt to destructure non-iterable instance.\nIn order to be iterable, non-array objects must have a [Symbol.iterator]() method."
            );
          })()
        );
      }
      function i(t, r) {
        (null == r || r > t.length) && (r = t.length);
        for (var e = 0, n = new Array(r); e < r; e++) n[e] = t[e];
        return n;
      }
      t.exports = function (t) {
        var r = this,
          e = {};
        return (
          Array.isArray(this.items)
            ? this.items.forEach(function (r, i) {
                var o = n(t(r, i), 2),
                  s = o[0],
                  u = o[1];
                e[s] = u;
              })
            : Object.keys(this.items).forEach(function (i) {
                var o = n(t(r.items[i], i), 2),
                  s = o[0],
                  u = o[1];
                e[s] = u;
              }),
          new this.constructor(e)
        );
      };
    },
    function (t, r, e) {
      "use strict";
      function n(t) {
        return (
          (function (t) {
            if (Array.isArray(t)) return i(t);
          })(t) ||
          (function (t) {
            if (
              ("undefined" != typeof Symbol && null != t[Symbol.iterator]) ||
              null != t["@@iterator"]
            )
              return Array.from(t);
          })(t) ||
          (function (t, r) {
            if (!t) return;
            if ("string" == typeof t) return i(t, r);
            var e = Object.prototype.toString.call(t).slice(8, -1);
            "Object" === e && t.constructor && (e = t.constructor.name);
            if ("Map" === e || "Set" === e) return Array.from(t);
            if (
              "Arguments" === e ||
              /^(?:Ui|I)nt(?:8|16|32)(?:Clamped)?Array$/.test(e)
            )
              return i(t, r);
          })(t) ||
          (function () {
            throw new TypeError(
              "Invalid attempt to spread non-iterable instance.\nIn order to be iterable, non-array objects must have a [Symbol.iterator]() method."
            );
          })()
        );
      }
      function i(t, r) {
        (null == r || r > t.length) && (r = t.length);
        for (var e = 0, n = new Array(r); e < r; e++) n[e] = t[e];
        return n;
      }
      t.exports = function (t) {
        if ("string" == typeof t) {
          var r = this.items.filter(function (r) {
            return void 0 !== r[t];
          });
          return Math.max.apply(
            Math,
            n(
              r.map(function (r) {
                return r[t];
              })
            )
          );
        }
        return Math.max.apply(Math, n(this.items));
      };
    },
    function (t, r, e) {
      "use strict";
      t.exports = function (t) {
        var r = this.items.length;
        return void 0 === t
          ? r % 2 == 0
            ? (this.items[r / 2 - 1] + this.items[r / 2]) / 2
            : this.items[Math.floor(r / 2)]
          : r % 2 == 0
          ? (this.items[r / 2 - 1][t] + this.items[r / 2][t]) / 2
          : this.items[Math.floor(r / 2)][t];
      };
    },
    function (t, r, e) {
      "use strict";
      t.exports = function (t) {
        var r = t;
        if (
          ("string" == typeof r && (r = [r]),
          Array.isArray(this.items) && Array.isArray(r))
        )
          return new this.constructor(this.items.concat(r));
        var e = JSON.parse(JSON.stringify(this.items));
        return (
          Object.keys(r).forEach(function (t) {
            e[t] = r[t];
          }),
          new this.constructor(e)
        );
      };
    },
    function (t, r, e) {
      "use strict";
      function n(t) {
        return (n =
          "function" == typeof Symbol && "symbol" == typeof Symbol.iterator
            ? function (t) {
                return typeof t;
              }
            : function (t) {
                return t &&
                  "function" == typeof Symbol &&
                  t.constructor === Symbol &&
                  t !== Symbol.prototype
                  ? "symbol"
                  : typeof t;
              })(t);
      }
      function i(t, r) {
        var e = Object.keys(t);
        if (Object.getOwnPropertySymbols) {
          var n = Object.getOwnPropertySymbols(t);
          r &&
            (n = n.filter(function (r) {
              return Object.getOwnPropertyDescriptor(t, r).enumerable;
            })),
            e.push.apply(e, n);
        }
        return e;
      }
      function o(t) {
        for (var r = 1; r < arguments.length; r++) {
          var e = null != arguments[r] ? arguments[r] : {};
          r % 2
            ? i(Object(e), !0).forEach(function (r) {
                s(t, r, e[r]);
              })
            : Object.getOwnPropertyDescriptors
            ? Object.defineProperties(t, Object.getOwnPropertyDescriptors(e))
            : i(Object(e)).forEach(function (r) {
                Object.defineProperty(
                  t,
                  r,
                  Object.getOwnPropertyDescriptor(e, r)
                );
              });
        }
        return t;
      }
      function s(t, r, e) {
        return (
          r in t
            ? Object.defineProperty(t, r, {
                value: e,
                enumerable: !0,
                configurable: !0,
                writable: !0,
              })
            : (t[r] = e),
          t
        );
      }
      t.exports = function (t) {
        var r = function t(r, e) {
          var i = {};
          return (
            Object.keys(o(o({}, r), e)).forEach(function (o) {
              void 0 === r[o] && void 0 !== e[o]
                ? (i[o] = e[o])
                : void 0 !== r[o] && void 0 === e[o]
                ? (i[o] = r[o])
                : void 0 !== r[o] &&
                  void 0 !== e[o] &&
                  (r[o] === e[o]
                    ? (i[o] = r[o])
                    : Array.isArray(r[o]) ||
                      "object" !== n(r[o]) ||
                      Array.isArray(e[o]) ||
                      "object" !== n(e[o])
                    ? (i[o] = [].concat(r[o], e[o]))
                    : (i[o] = t(r[o], e[o])));
            }),
            i
          );
        };
        return t
          ? "Collection" === t.constructor.name
            ? new this.constructor(r(this.items, t.all()))
            : new this.constructor(r(this.items, t))
          : this;
      };
    },
    function (t, r, e) {
      "use strict";
      function n(t) {
        return (
          (function (t) {
            if (Array.isArray(t)) return i(t);
          })(t) ||
          (function (t) {
            if (
              ("undefined" != typeof Symbol && null != t[Symbol.iterator]) ||
              null != t["@@iterator"]
            )
              return Array.from(t);
          })(t) ||
          (function (t, r) {
            if (!t) return;
            if ("string" == typeof t) return i(t, r);
            var e = Object.prototype.toString.call(t).slice(8, -1);
            "Object" === e && t.constructor && (e = t.constructor.name);
            if ("Map" === e || "Set" === e) return Array.from(t);
            if (
              "Arguments" === e ||
              /^(?:Ui|I)nt(?:8|16|32)(?:Clamped)?Array$/.test(e)
            )
              return i(t, r);
          })(t) ||
          (function () {
            throw new TypeError(
              "Invalid attempt to spread non-iterable instance.\nIn order to be iterable, non-array objects must have a [Symbol.iterator]() method."
            );
          })()
        );
      }
      function i(t, r) {
        (null == r || r > t.length) && (r = t.length);
        for (var e = 0, n = new Array(r); e < r; e++) n[e] = t[e];
        return n;
      }
      t.exports = function (t) {
        if (void 0 !== t) {
          var r = this.items.filter(function (r) {
            return void 0 !== r[t];
          });
          return Math.min.apply(
            Math,
            n(
              r.map(function (r) {
                return r[t];
              })
            )
          );
        }
        return Math.min.apply(Math, n(this.items));
      };
    },
    function (t, r, e) {
      "use strict";
      t.exports = function (t) {
        var r = [],
          e = 1;
        return this.items.length
          ? (this.items.forEach(function (n) {
              var i = r.filter(function (r) {
                return void 0 !== t ? r.key === n[t] : r.key === n;
              });
              if (i.length) {
                i[0].count += 1;
                var o = i[0].count;
                o > e && (e = o);
              } else void 0 !== t ? r.push({ key: n[t], count: 1 }) : r.push({ key: n, count: 1 });
            }),
            r
              .filter(function (t) {
                return t.count === e;
              })
              .map(function (t) {
                return t.key;
              }))
          : null;
      };
    },
    function (t, r, e) {
      "use strict";
      var n = e(1);
      t.exports = function (t) {
        var r =
            arguments.length > 1 && void 0 !== arguments[1] ? arguments[1] : 0,
          e = n(this.items),
          i = e.slice(r).filter(function (r, e) {
            return e % t == 0;
          });
        return new this.constructor(i);
      };
    },
    function (t, r, e) {
      "use strict";
      var n = e(3);
      t.exports = function () {
        for (
          var t = this, r = arguments.length, e = new Array(r), i = 0;
          i < r;
          i++
        )
          e[i] = arguments[i];
        var o = n(e);
        if (Array.isArray(this.items)) {
          var s = this.items.filter(function (t) {
            return -1 !== o.indexOf(t);
          });
          return new this.constructor(s);
        }
        var u = {};
        return (
          Object.keys(this.items).forEach(function (r) {
            -1 !== o.indexOf(r) && (u[r] = t.items[r]);
          }),
          new this.constructor(u)
        );
      };
    },
    function (t, r, e) {
      "use strict";
      var n = e(5);
      t.exports = function (t, r) {
        var e = Math.abs(t),
          i = this.count();
        if (e <= i) return this;
        for (
          var o = e - i,
            s = n(this.items),
            u = Array.isArray(this.items),
            c = t < 0,
            f = 0;
          f < o;

        )
          u
            ? c
              ? s.unshift(r)
              : s.push(r)
            : void 0 !== s[f]
            ? (o += 1)
            : (s[f] = r),
            (f += 1);
        return new this.constructor(s);
      };
    },
    function (t, r, e) {
      "use strict";
      t.exports = function (t) {
        var r,
          e = this;
        return (
          Array.isArray(this.items)
            ? ((r = [new this.constructor([]), new this.constructor([])]),
              this.items.forEach(function (e) {
                !0 === t(e) ? r[0].push(e) : r[1].push(e);
              }))
            : ((r = [new this.constructor({}), new this.constructor({})]),
              Object.keys(this.items).forEach(function (n) {
                var i = e.items[n];
                !0 === t(i) ? r[0].put(n, i) : r[1].put(n, i);
              })),
          new this.constructor(r)
        );
      };
    },
    function (t, r, e) {
      "use strict";
      t.exports = function (t) {
        return t(this);
      };
    },
    function (t, r, e) {
      "use strict";
      var n = e(0),
        i = n.isArray,
        o = n.isObject,
        s = e(2);
      t.exports = function (t, r) {
        if (-1 !== t.indexOf("*")) {
          var e =
              ((h = this.items),
              (y = {}),
              h.forEach(function (t, r) {
                !(function t(r, e) {
                  o(r)
                    ? Object.keys(r).forEach(function (n) {
                        t(r[n], "".concat(e, ".").concat(n));
                      })
                    : i(r) &&
                      r.forEach(function (r, n) {
                        t(r, "".concat(e, ".").concat(n));
                      }),
                    (y[e] = r);
                })(t, r);
              }),
              y),
            n = [];
          if (void 0 !== r) {
            var u = new RegExp("0.".concat(r), "g"),
              c = "0.".concat(r).split(".").length;
            Object.keys(e).forEach(function (t) {
              var r = t.match(u);
              if (r) {
                var i = r[0];
                i.split(".").length === c && n.push(e[i]);
              }
            });
          }
          var f = [],
            a = new RegExp("0.".concat(t), "g"),
            p = "0.".concat(t).split(".").length;
          if (
            (Object.keys(e).forEach(function (t) {
              var r = t.match(a);
              if (r) {
                var n = r[0];
                n.split(".").length === p && f.push(e[n]);
              }
            }),
            void 0 !== r)
          ) {
            var l = {};
            return (
              this.items.forEach(function (t, r) {
                l[n[r] || ""] = f;
              }),
              new this.constructor(l)
            );
          }
          return new this.constructor([f]);
        }
        var h, y;
        if (void 0 !== r) {
          var m = {};
          return (
            this.items.forEach(function (e) {
              void 0 !== s(e, t)
                ? (m[e[r] || ""] = s(e, t))
                : (m[e[r] || ""] = null);
            }),
            new this.constructor(m)
          );
        }
        return this.map(function (r) {
          return void 0 !== s(r, t) ? s(r, t) : null;
        });
      };
    },
    function (t, r, e) {
      "use strict";
      var n = e(0),
        i = n.isArray,
        o = n.isObject,
        s = e(7);
      t.exports = function () {
        var t = this,
          r =
            arguments.length > 0 && void 0 !== arguments[0] ? arguments[0] : 1;
        if (this.isEmpty()) return null;
        if (i(this.items))
          return 1 === r
            ? this.items.pop()
            : new this.constructor(this.items.splice(-r));
        if (o(this.items)) {
          var e = Object.keys(this.items);
          if (1 === r) {
            var n = e[e.length - 1],
              u = this.items[n];
            return s(this.items, n), u;
          }
          var c = e.slice(-r),
            f = c.reduce(function (r, e) {
              return (r[e] = t.items[e]), r;
            }, {});
          return s(this.items, c), new this.constructor(f);
        }
        return null;
      };
    },
    function (t, r, e) {
      "use strict";
      t.exports = function (t, r) {
        return void 0 !== r ? this.put(r, t) : (this.items.unshift(t), this);
      };
    },
    function (t, r, e) {
      "use strict";
      var n = e(0).isFunction;
      t.exports = function (t, r) {
        var e = this.items[t] || null;
        return (
          e || void 0 === r || (e = n(r) ? r() : r), delete this.items[t], e
        );
      };
    },
    function (t, r, e) {
      "use strict";
      t.exports = function () {
        var t;
        return (t = this.items).push.apply(t, arguments), this;
      };
    },
    function (t, r, e) {
      "use strict";
      t.exports = function (t, r) {
        return (this.items[t] = r), this;
      };
    },
    function (t, r, e) {
      "use strict";
      var n = e(1);
      t.exports = function () {
        var t =
            arguments.length > 0 && void 0 !== arguments[0]
              ? arguments[0]
              : null,
          r = n(this.items),
          e = new this.constructor(r).shuffle();
        return t !== parseInt(t, 10) ? e.first() : e.take(t);
      };
    },
    function (t, r, e) {
      "use strict";
      t.exports = function (t, r) {
        var e = this,
          n = null;
        return (
          void 0 !== r && (n = r),
          Array.isArray(this.items)
            ? this.items.forEach(function (r) {
                n = t(n, r);
              })
            : Object.keys(this.items).forEach(function (r) {
                n = t(n, e.items[r], r);
              }),
          n
        );
      };
    },
    function (t, r, e) {
      "use strict";
      t.exports = function (t) {
        return new this.constructor(this.items).filter(function (r) {
          return !t(r);
        });
      };
    },
    function (t, r, e) {
      "use strict";
      function n(t, r) {
        var e = Object.keys(t);
        if (Object.getOwnPropertySymbols) {
          var n = Object.getOwnPropertySymbols(t);
          r &&
            (n = n.filter(function (r) {
              return Object.getOwnPropertyDescriptor(t, r).enumerable;
            })),
            e.push.apply(e, n);
        }
        return e;
      }
      function i(t) {
        for (var r = 1; r < arguments.length; r++) {
          var e = null != arguments[r] ? arguments[r] : {};
          r % 2
            ? n(Object(e), !0).forEach(function (r) {
                o(t, r, e[r]);
              })
            : Object.getOwnPropertyDescriptors
            ? Object.defineProperties(t, Object.getOwnPropertyDescriptors(e))
            : n(Object(e)).forEach(function (r) {
                Object.defineProperty(
                  t,
                  r,
                  Object.getOwnPropertyDescriptor(e, r)
                );
              });
        }
        return t;
      }
      function o(t, r, e) {
        return (
          r in t
            ? Object.defineProperty(t, r, {
                value: e,
                enumerable: !0,
                configurable: !0,
                writable: !0,
              })
            : (t[r] = e),
          t
        );
      }
      t.exports = function (t) {
        if (!t) return this;
        if (Array.isArray(t)) {
          var r = this.items.map(function (r, e) {
            return t[e] || r;
          });
          return new this.constructor(r);
        }
        if ("Collection" === t.constructor.name) {
          var e = i(i({}, this.items), t.all());
          return new this.constructor(e);
        }
        var n = i(i({}, this.items), t);
        return new this.constructor(n);
      };
    },
    function (t, r, e) {
      "use strict";
      function n(t) {
        return (n =
          "function" == typeof Symbol && "symbol" == typeof Symbol.iterator
            ? function (t) {
                return typeof t;
              }
            : function (t) {
                return t &&
                  "function" == typeof Symbol &&
                  t.constructor === Symbol &&
                  t !== Symbol.prototype
                  ? "symbol"
                  : typeof t;
              })(t);
      }
      function i(t, r) {
        var e = Object.keys(t);
        if (Object.getOwnPropertySymbols) {
          var n = Object.getOwnPropertySymbols(t);
          r &&
            (n = n.filter(function (r) {
              return Object.getOwnPropertyDescriptor(t, r).enumerable;
            })),
            e.push.apply(e, n);
        }
        return e;
      }
      function o(t) {
        for (var r = 1; r < arguments.length; r++) {
          var e = null != arguments[r] ? arguments[r] : {};
          r % 2
            ? i(Object(e), !0).forEach(function (r) {
                s(t, r, e[r]);
              })
            : Object.getOwnPropertyDescriptors
            ? Object.defineProperties(t, Object.getOwnPropertyDescriptors(e))
            : i(Object(e)).forEach(function (r) {
                Object.defineProperty(
                  t,
                  r,
                  Object.getOwnPropertyDescriptor(e, r)
                );
              });
        }
        return t;
      }
      function s(t, r, e) {
        return (
          r in t
            ? Object.defineProperty(t, r, {
                value: e,
                enumerable: !0,
                configurable: !0,
                writable: !0,
              })
            : (t[r] = e),
          t
        );
      }
      t.exports = function (t) {
        var r = function t(r, e) {
          var i = o({}, r);
          return (
            Object.keys(o(o({}, r), e)).forEach(function (s) {
              Array.isArray(e[s]) || "object" !== n(e[s])
                ? void 0 === r[s] && void 0 !== e[s]
                  ? "object" === n(r[s])
                    ? (i[s] = o({}, e[s]))
                    : (i[s] = e[s])
                  : void 0 !== r[s] && void 0 === e[s]
                  ? "object" === n(r[s])
                    ? (i[s] = o({}, r[s]))
                    : (i[s] = r[s])
                  : void 0 !== r[s] &&
                    void 0 !== e[s] &&
                    ("object" === n(e[s])
                      ? (i[s] = o({}, e[s]))
                      : (i[s] = e[s]))
                : (i[s] = t(r[s], e[s]));
            }),
            i
          );
        };
        return t
          ? Array.isArray(t) || "object" === n(t)
            ? "Collection" === t.constructor.name
              ? new this.constructor(r(this.items, t.all()))
              : new this.constructor(r(this.items, t))
            : new this.constructor(r(this.items, [t]))
          : this;
      };
    },
    function (t, r, e) {
      "use strict";
      t.exports = function () {
        var t = [].concat(this.items).reverse();
        return new this.constructor(t);
      };
    },
    function (t, r, e) {
      "use strict";
      var n = e(0),
        i = n.isArray,
        o = n.isObject,
        s = n.isFunction;
      t.exports = function (t, r) {
        var e,
          n = this,
          u = function (e, i) {
            return s(t)
              ? t(n.items[i], i)
              : r
              ? n.items[i] === t
              : n.items[i] == t;
          };
        return (
          i(this.items)
            ? (e = this.items.findIndex(u))
            : o(this.items) &&
              (e = Object.keys(this.items).find(function (t) {
                return u(n.items[t], t);
              })),
          !(void 0 === e || e < 0) && e
        );
      };
    },
    function (t, r, e) {
      "use strict";
      var n = e(0),
        i = n.isArray,
        o = n.isObject,
        s = e(7);
      t.exports = function () {
        var t = this,
          r =
            arguments.length > 0 && void 0 !== arguments[0] ? arguments[0] : 1;
        if (this.isEmpty()) return null;
        if (i(this.items))
          return 1 === r
            ? this.items.shift()
            : new this.constructor(this.items.splice(0, r));
        if (o(this.items)) {
          if (1 === r) {
            var e = Object.keys(this.items)[0],
              n = this.items[e];
            return delete this.items[e], n;
          }
          var u = Object.keys(this.items),
            c = u.slice(0, r),
            f = c.reduce(function (r, e) {
              return (r[e] = t.items[e]), r;
            }, {});
          return s(this.items, c), new this.constructor(f);
        }
        return null;
      };
    },
    function (t, r, e) {
      "use strict";
      var n = e(1);
      t.exports = function () {
        var t,
          r,
          e,
          i = n(this.items);
        for (e = i.length; e; e -= 1)
          (t = Math.floor(Math.random() * e)),
            (r = i[e - 1]),
            (i[e - 1] = i[t]),
            (i[t] = r);
        return (this.items = i), this;
      };
    },
    function (t, r, e) {
      "use strict";
      var n = e(0).isObject;
      t.exports = function (t) {
        var r = this;
        return n(this.items)
          ? new this.constructor(
              Object.keys(this.items).reduce(function (e, n, i) {
                return i + 1 > t && (e[n] = r.items[n]), e;
              }, {})
            )
          : new this.constructor(this.items.slice(t));
      };
    },
    function (t, r, e) {
      "use strict";
      var n = e(0),
        i = n.isArray,
        o = n.isObject,
        s = n.isFunction;
      t.exports = function (t) {
        var r,
          e = this,
          n = null,
          u = function (r) {
            return r === t;
          };
        return (
          s(t) && (u = t),
          i(this.items) &&
            (r = this.items.filter(function (t) {
              return !0 !== n && (n = u(t)), n;
            })),
          o(this.items) &&
            (r = Object.keys(this.items).reduce(function (t, r) {
              return (
                !0 !== n && (n = u(e.items[r])),
                !1 !== n && (t[r] = e.items[r]),
                t
              );
            }, {})),
          new this.constructor(r)
        );
      };
    },
    function (t, r, e) {
      "use strict";
      var n = e(0),
        i = n.isArray,
        o = n.isObject,
        s = n.isFunction;
      t.exports = function (t) {
        var r,
          e = this,
          n = null,
          u = function (r) {
            return r === t;
          };
        return (
          s(t) && (u = t),
          i(this.items) &&
            (r = this.items.filter(function (t) {
              return !0 !== n && (n = !u(t)), n;
            })),
          o(this.items) &&
            (r = Object.keys(this.items).reduce(function (t, r) {
              return (
                !0 !== n && (n = !u(e.items[r])),
                !1 !== n && (t[r] = e.items[r]),
                t
              );
            }, {})),
          new this.constructor(r)
        );
      };
    },
    function (t, r, e) {
      "use strict";
      t.exports = function (t, r) {
        var e = this.items.slice(t);
        return void 0 !== r && (e = e.slice(0, r)), new this.constructor(e);
      };
    },
    function (t, r, e) {
      "use strict";
      var n = e(0).isFunction;
      t.exports = function (t, r, e) {
        var i;
        if ((i = n(t) ? this.filter(t) : this.where(t, r, e)).isEmpty())
          throw new Error("Item not found.");
        if (i.count() > 1) throw new Error("Multiple items found.");
        return i.first();
      };
    },
    function (t, r, e) {
      "use strict";
      var n = e(6);
      t.exports = n;
    },
    function (t, r, e) {
      "use strict";
      t.exports = function (t) {
        var r = [].concat(this.items);
        return (
          void 0 === t
            ? this.every(function (t) {
                return "number" == typeof t;
              })
              ? r.sort(function (t, r) {
                  return t - r;
                })
              : r.sort()
            : r.sort(t),
          new this.constructor(r)
        );
      };
    },
    function (t, r, e) {
      "use strict";
      t.exports = function () {
        return this.sort().reverse();
      };
    },
    function (t, r, e) {
      "use strict";
      var n = e(2),
        i = e(0).isFunction;
      t.exports = function (t) {
        var r = [].concat(this.items),
          e = function (r) {
            return i(t) ? t(r) : n(r, t);
          };
        return (
          r.sort(function (t, r) {
            var n = e(t),
              i = e(r);
            return null == n ? 1 : null == i || n < i ? -1 : n > i ? 1 : 0;
          }),
          new this.constructor(r)
        );
      };
    },
    function (t, r, e) {
      "use strict";
      t.exports = function (t) {
        return this.sortBy(t).reverse();
      };
    },
    function (t, r, e) {
      "use strict";
      t.exports = function () {
        var t = this,
          r = {};
        return (
          Object.keys(this.items)
            .sort()
            .forEach(function (e) {
              r[e] = t.items[e];
            }),
          new this.constructor(r)
        );
      };
    },
    function (t, r, e) {
      "use strict";
      t.exports = function () {
        var t = this,
          r = {};
        return (
          Object.keys(this.items)
            .sort()
            .reverse()
            .forEach(function (e) {
              r[e] = t.items[e];
            }),
          new this.constructor(r)
        );
      };
    },
    function (t, r, e) {
      "use strict";
      t.exports = function (t, r, e) {
        var n = this.slice(t, r);
        if (((this.items = this.diff(n.all()).all()), Array.isArray(e)))
          for (var i = 0, o = e.length; i < o; i += 1)
            this.items.splice(t + i, 0, e[i]);
        return n;
      };
    },
    function (t, r, e) {
      "use strict";
      t.exports = function (t) {
        for (
          var r = Math.round(this.items.length / t),
            e = JSON.parse(JSON.stringify(this.items)),
            n = [],
            i = 0;
          i < t;
          i += 1
        )
          n.push(new this.constructor(e.splice(0, r)));
        return new this.constructor(n);
      };
    },
    function (t, r, e) {
      "use strict";
      var n = e(1),
        i = e(0).isFunction;
      t.exports = function (t) {
        var r = n(this.items),
          e = 0;
        if (void 0 === t)
          for (var o = 0, s = r.length; o < s; o += 1) e += parseFloat(r[o]);
        else if (i(t))
          for (var u = 0, c = r.length; u < c; u += 1) e += parseFloat(t(r[u]));
        else
          for (var f = 0, a = r.length; f < a; f += 1) e += parseFloat(r[f][t]);
        return parseFloat(e.toPrecision(12));
      };
    },
    function (t, r, e) {
      "use strict";
      function n(t) {
        return (n =
          "function" == typeof Symbol && "symbol" == typeof Symbol.iterator
            ? function (t) {
                return typeof t;
              }
            : function (t) {
                return t &&
                  "function" == typeof Symbol &&
                  t.constructor === Symbol &&
                  t !== Symbol.prototype
                  ? "symbol"
                  : typeof t;
              })(t);
      }
      t.exports = function (t) {
        var r = this;
        if (!Array.isArray(this.items) && "object" === n(this.items)) {
          var e,
            i = Object.keys(this.items);
          e = t < 0 ? i.slice(t) : i.slice(0, t);
          var o = {};
          return (
            i.forEach(function (t) {
              -1 !== e.indexOf(t) && (o[t] = r.items[t]);
            }),
            new this.constructor(o)
          );
        }
        return t < 0
          ? new this.constructor(this.items.slice(t))
          : new this.constructor(this.items.slice(0, t));
      };
    },
    function (t, r, e) {
      "use strict";
      var n = e(0),
        i = n.isArray,
        o = n.isObject,
        s = n.isFunction;
      t.exports = function (t) {
        var r,
          e = this,
          n = null,
          u = function (r) {
            return r === t;
          };
        return (
          s(t) && (u = t),
          i(this.items) &&
            (r = this.items.filter(function (t) {
              return !1 !== n && (n = !u(t)), n;
            })),
          o(this.items) &&
            (r = Object.keys(this.items).reduce(function (t, r) {
              return (
                !1 !== n && (n = !u(e.items[r])),
                !1 !== n && (t[r] = e.items[r]),
                t
              );
            }, {})),
          new this.constructor(r)
        );
      };
    },
    function (t, r, e) {
      "use strict";
      var n = e(0),
        i = n.isArray,
        o = n.isObject,
        s = n.isFunction;
      t.exports = function (t) {
        var r,
          e = this,
          n = null,
          u = function (r) {
            return r === t;
          };
        return (
          s(t) && (u = t),
          i(this.items) &&
            (r = this.items.filter(function (t) {
              return !1 !== n && (n = u(t)), n;
            })),
          o(this.items) &&
            (r = Object.keys(this.items).reduce(function (t, r) {
              return (
                !1 !== n && (n = u(e.items[r])),
                !1 !== n && (t[r] = e.items[r]),
                t
              );
            }, {})),
          new this.constructor(r)
        );
      };
    },
    function (t, r, e) {
      "use strict";
      t.exports = function (t) {
        return t(this), this;
      };
    },
    function (t, r, e) {
      "use strict";
      t.exports = function (t, r) {
        for (var e = 1; e <= t; e += 1) this.items.push(r(e));
        return this;
      };
    },
    function (t, r, e) {
      "use strict";
      t.exports = function () {
        var t = this.constructor;
        if (Array.isArray(this.items)) {
          var r = [];
          return (
            this.items.forEach(function (e) {
              !(function r(e, n) {
                var i = [];
                e instanceof t
                  ? (e.items.forEach(function (t) {
                      return r(t, i);
                    }),
                    n.push(i))
                  : Array.isArray(e)
                  ? (e.forEach(function (t) {
                      return r(t, i);
                    }),
                    n.push(i))
                  : n.push(e);
              })(e, r);
            }),
            r
          );
        }
        return this.values().all();
      };
    },
    function (t, r, e) {
      "use strict";
      function n(t) {
        return (n =
          "function" == typeof Symbol && "symbol" == typeof Symbol.iterator
            ? function (t) {
                return typeof t;
              }
            : function (t) {
                return t &&
                  "function" == typeof Symbol &&
                  t.constructor === Symbol &&
                  t !== Symbol.prototype
                  ? "symbol"
                  : typeof t;
              })(t);
      }
      t.exports = function () {
        return "object" !== n(this.items) || Array.isArray(this.items)
          ? JSON.stringify(this.toArray())
          : JSON.stringify(this.all());
      };
    },
    function (t, r, e) {
      "use strict";
      t.exports = function (t) {
        var r = this;
        if (Array.isArray(this.items)) this.items = this.items.map(t);
        else {
          var e = {};
          Object.keys(this.items).forEach(function (n) {
            e[n] = t(r.items[n], n);
          }),
            (this.items = e);
        }
        return this;
      };
    },
    function (t, r, e) {
      "use strict";
      function n(t, r) {
        var e = Object.keys(t);
        if (Object.getOwnPropertySymbols) {
          var n = Object.getOwnPropertySymbols(t);
          r &&
            (n = n.filter(function (r) {
              return Object.getOwnPropertyDescriptor(t, r).enumerable;
            })),
            e.push.apply(e, n);
        }
        return e;
      }
      function i(t) {
        for (var r = 1; r < arguments.length; r++) {
          var e = null != arguments[r] ? arguments[r] : {};
          r % 2
            ? n(Object(e), !0).forEach(function (r) {
                o(t, r, e[r]);
              })
            : Object.getOwnPropertyDescriptors
            ? Object.defineProperties(t, Object.getOwnPropertyDescriptors(e))
            : n(Object(e)).forEach(function (r) {
                Object.defineProperty(
                  t,
                  r,
                  Object.getOwnPropertyDescriptor(e, r)
                );
              });
        }
        return t;
      }
      function o(t, r, e) {
        return (
          r in t
            ? Object.defineProperty(t, r, {
                value: e,
                enumerable: !0,
                configurable: !0,
                writable: !0,
              })
            : (t[r] = e),
          t
        );
      }
      t.exports = function () {
        var t = this;
        if (Array.isArray(this.items)) return this;
        var r = {};
        return (
          Object.keys(this.items).forEach(function (e) {
            if (-1 !== e.indexOf(".")) {
              var n = r;
              e.split(".").reduce(function (r, n, i, o) {
                return (
                  r[n] || (r[n] = {}),
                  i === o.length - 1 && (r[n] = t.items[e]),
                  r[n]
                );
              }, n),
                (r = i(i({}, r), n));
            } else r[e] = t.items[e];
          }),
          new this.constructor(r)
        );
      };
    },
    function (t, r, e) {
      "use strict";
      t.exports = function (t, r, e) {
        t ? e(this) : r(this);
      };
    },
    function (t, r, e) {
      "use strict";
      t.exports = function (t) {
        var r = this,
          e = JSON.parse(JSON.stringify(this.items));
        return (
          Object.keys(t).forEach(function (n) {
            void 0 === r.items[n] && (e[n] = t[n]);
          }),
          new this.constructor(e)
        );
      };
    },
    function (t, r, e) {
      "use strict";
      var n = e(0).isFunction;
      t.exports = function (t) {
        var r;
        if (void 0 === t)
          r = this.items.filter(function (t, r, e) {
            return e.indexOf(t) === r;
          });
        else {
          r = [];
          for (var e = [], i = 0, o = this.items.length; i < o; i += 1) {
            var s = void 0;
            (s = n(t) ? t(this.items[i]) : this.items[i][t]),
              -1 === e.indexOf(s) && (r.push(this.items[i]), e.push(s));
          }
        }
        return new this.constructor(r);
      };
    },
    function (t, r, e) {
      "use strict";
      t.exports = function (t) {
        return t instanceof this.constructor ? t.all() : t;
      };
    },
    function (t, r, e) {
      "use strict";
      var n = e(1);
      t.exports = function () {
        return new this.constructor(n(this.items));
      };
    },
    function (t, r, e) {
      "use strict";
      t.exports = function (t, r, e) {
        return t ? r(this, t) : e ? e(this, t) : this;
      };
    },
    function (t, r, e) {
      "use strict";
      var n = e(1),
        i = e(2);
      t.exports = function (t, r, e) {
        var o = r,
          s = e,
          u = n(this.items);
        if (void 0 === r || !0 === r)
          return new this.constructor(
            u.filter(function (r) {
              return i(r, t);
            })
          );
        if (!1 === r)
          return new this.constructor(
            u.filter(function (r) {
              return !i(r, t);
            })
          );
        void 0 === e && ((s = r), (o = "==="));
        var c = u.filter(function (r) {
          switch (o) {
            case "==":
              return i(r, t) === Number(s) || i(r, t) === s.toString();
            default:
            case "===":
              return i(r, t) === s;
            case "!=":
            case "<>":
              return i(r, t) !== Number(s) && i(r, t) !== s.toString();
            case "!==":
              return i(r, t) !== s;
            case "<":
              return i(r, t) < s;
            case "<=":
              return i(r, t) <= s;
            case ">":
              return i(r, t) > s;
            case ">=":
              return i(r, t) >= s;
          }
        });
        return new this.constructor(c);
      };
    },
    function (t, r, e) {
      "use strict";
      t.exports = function (t, r) {
        return this.where(t, ">=", r[0]).where(t, "<=", r[r.length - 1]);
      };
    },
    function (t, r, e) {
      "use strict";
      var n = e(1),
        i = e(2);
      t.exports = function (t, r) {
        var e = n(r),
          o = this.items.filter(function (r) {
            return -1 !== e.indexOf(i(r, t));
          });
        return new this.constructor(o);
      };
    },
    function (t, r, e) {
      "use strict";
      t.exports = function (t) {
        return this.filter(function (r) {
          return r instanceof t;
        });
      };
    },
    function (t, r, e) {
      "use strict";
      var n = e(2);
      t.exports = function (t, r) {
        return this.filter(function (e) {
          return n(e, t) < r[0] || n(e, t) > r[r.length - 1];
        });
      };
    },
    function (t, r, e) {
      "use strict";
      var n = e(1),
        i = e(2);
      t.exports = function (t, r) {
        var e = n(r),
          o = this.items.filter(function (r) {
            return -1 === e.indexOf(i(r, t));
          });
        return new this.constructor(o);
      };
    },
    function (t, r, e) {
      "use strict";
      t.exports = function () {
        var t =
          arguments.length > 0 && void 0 !== arguments[0] ? arguments[0] : null;
        return this.where(t, "===", null);
      };
    },
    function (t, r, e) {
      "use strict";
      t.exports = function () {
        var t =
          arguments.length > 0 && void 0 !== arguments[0] ? arguments[0] : null;
        return this.where(t, "!==", null);
      };
    },
    function (t, r, e) {
      "use strict";
      function n(t) {
        return (n =
          "function" == typeof Symbol && "symbol" == typeof Symbol.iterator
            ? function (t) {
                return typeof t;
              }
            : function (t) {
                return t &&
                  "function" == typeof Symbol &&
                  t.constructor === Symbol &&
                  t !== Symbol.prototype
                  ? "symbol"
                  : typeof t;
              })(t);
      }
      t.exports = function (t) {
        return t instanceof this.constructor
          ? t
          : "object" === n(t)
          ? new this.constructor(t)
          : new this.constructor([t]);
      };
    },
    function (t, r, e) {
      "use strict";
      t.exports = function (t) {
        var r = this,
          e = t;
        e instanceof this.constructor && (e = e.all());
        var n = this.items.map(function (t, n) {
          return new r.constructor([t, e[n]]);
        });
        return new this.constructor(n);
      };
    },
  ]);
  return {
    collect: collect,
  };
})();
