// Transcrypt'ed from Python, 2020-04-28 21:58:32
import {AssertionError, AttributeError, BaseException, DeprecationWarning, Exception, IndexError, IterableError, KeyError, NotImplementedError, RuntimeWarning, StopIteration, UserWarning, ValueError, Warning, __JsIterator__, __PyIterator__, __Terminal__, __add__, __and__, __call__, __class__, __envir__, __eq__, __floordiv__, __ge__, __get__, __getcm__, __getitem__, __getslice__, __getsm__, __gt__, __i__, __iadd__, __iand__, __idiv__, __ijsmod__, __ilshift__, __imatmul__, __imod__, __imul__, __in__, __init__, __ior__, __ipow__, __irshift__, __isub__, __ixor__, __jsUsePyNext__, __jsmod__, __k__, __kwargtrans__, __le__, __lshift__, __lt__, __matmul__, __mergefields__, __mergekwargtrans__, __mod__, __mul__, __ne__, __neg__, __nest__, __or__, __pow__, __pragma__, __proxy__, __pyUseJsNext__, __rshift__, __setitem__, __setproperty__, __setslice__, __sort__, __specialattrib__, __sub__, __super__, __t__, __terminal__, __truediv__, __withblock__, __xor__, abs, all, any, assert, bool, bytearray, bytes, callable, chr, copy, deepcopy, delattr, dict, dir, divmod, enumerate, filter, float, getattr, hasattr, input, int, isinstance, issubclass, len, list, map, max, min, object, ord, print, property, py_TypeError, py_iter, py_metatype, py_next, py_reversed, py_typeof, range, repr, round, set, setattr, sorted, str, sum, tuple, zip} from './org.transcrypt.__runtime__.js';
var __name__ = 'math';
export var pi = Math.PI;
export var e = Math.E;
export var exp = Math.exp;
export var expm1 = function (x) {
	if (arguments.length) {
		var __ilastarg0__ = arguments.length - 1;
		if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
			var __allkwargs0__ = arguments [__ilastarg0__--];
			for (var __attrib0__ in __allkwargs0__) {
				switch (__attrib0__) {
					case 'x': var x = __allkwargs0__ [__attrib0__]; break;
				}
			}
		}
	}
	else {
	}
	return Math.exp (x) - 1;
};
export var log = function (x, base) {
	if (arguments.length) {
		var __ilastarg0__ = arguments.length - 1;
		if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
			var __allkwargs0__ = arguments [__ilastarg0__--];
			for (var __attrib0__ in __allkwargs0__) {
				switch (__attrib0__) {
					case 'x': var x = __allkwargs0__ [__attrib0__]; break;
					case 'base': var base = __allkwargs0__ [__attrib0__]; break;
				}
			}
		}
	}
	else {
	}
	return (base === undefined ? Math.log (x) : Math.log (x) / Math.log (base));
};
export var log1p = function (x) {
	if (arguments.length) {
		var __ilastarg0__ = arguments.length - 1;
		if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
			var __allkwargs0__ = arguments [__ilastarg0__--];
			for (var __attrib0__ in __allkwargs0__) {
				switch (__attrib0__) {
					case 'x': var x = __allkwargs0__ [__attrib0__]; break;
				}
			}
		}
	}
	else {
	}
	return Math.log (x + 1);
};
export var log2 = function (x) {
	if (arguments.length) {
		var __ilastarg0__ = arguments.length - 1;
		if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
			var __allkwargs0__ = arguments [__ilastarg0__--];
			for (var __attrib0__ in __allkwargs0__) {
				switch (__attrib0__) {
					case 'x': var x = __allkwargs0__ [__attrib0__]; break;
				}
			}
		}
	}
	else {
	}
	return Math.log (x) / Math.LN2;
};
export var log10 = function (x) {
	if (arguments.length) {
		var __ilastarg0__ = arguments.length - 1;
		if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
			var __allkwargs0__ = arguments [__ilastarg0__--];
			for (var __attrib0__ in __allkwargs0__) {
				switch (__attrib0__) {
					case 'x': var x = __allkwargs0__ [__attrib0__]; break;
				}
			}
		}
	}
	else {
	}
	return Math.log (x) / Math.LN10;
};
export var pow = Math.pow;
export var sqrt = Math.sqrt;
export var sin = Math.sin;
export var cos = Math.cos;
export var tan = Math.tan;
export var asin = Math.asin;
export var acos = Math.acos;
export var atan = Math.atan;
export var atan2 = Math.atan2;
export var hypot = Math.hypot;
export var degrees = function (x) {
	if (arguments.length) {
		var __ilastarg0__ = arguments.length - 1;
		if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
			var __allkwargs0__ = arguments [__ilastarg0__--];
			for (var __attrib0__ in __allkwargs0__) {
				switch (__attrib0__) {
					case 'x': var x = __allkwargs0__ [__attrib0__]; break;
				}
			}
		}
	}
	else {
	}
	return (x * 180) / Math.PI;
};
export var radians = function (x) {
	if (arguments.length) {
		var __ilastarg0__ = arguments.length - 1;
		if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
			var __allkwargs0__ = arguments [__ilastarg0__--];
			for (var __attrib0__ in __allkwargs0__) {
				switch (__attrib0__) {
					case 'x': var x = __allkwargs0__ [__attrib0__]; break;
				}
			}
		}
	}
	else {
	}
	return (x * Math.PI) / 180;
};
export var sinh = Math.sinh;
export var cosh = Math.cosh;
export var tanh = Math.tanh;
export var asinh = Math.asinh;
export var acosh = Math.acosh;
export var atanh = Math.atanh;
export var floor = Math.floor;
export var ceil = Math.ceil;
export var trunc = Math.trunc;
export var isnan = isNaN;
export var inf = Infinity;
export var nan = NaN;
export var modf = function (n) {
	if (arguments.length) {
		var __ilastarg0__ = arguments.length - 1;
		if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
			var __allkwargs0__ = arguments [__ilastarg0__--];
			for (var __attrib0__ in __allkwargs0__) {
				switch (__attrib0__) {
					case 'n': var n = __allkwargs0__ [__attrib0__]; break;
				}
			}
		}
	}
	else {
	}
	var sign = (n >= 0 ? 1 : -(1));
	var __left0__ = divmod (abs (n), 1);
	var f = __left0__ [0];
	var mod = __left0__ [1];
	return tuple ([mod * sign, f * sign]);
};

//# sourceMappingURL=math.map