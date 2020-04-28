// Transcrypt'ed from Python, 2020-04-28 19:59:50
import {AssertionError, AttributeError, BaseException, DeprecationWarning, Exception, IndexError, IterableError, KeyError, NotImplementedError, RuntimeWarning, StopIteration, UserWarning, ValueError, Warning, __JsIterator__, __PyIterator__, __Terminal__, __add__, __and__, __call__, __class__, __envir__, __eq__, __floordiv__, __ge__, __get__, __getcm__, __getitem__, __getslice__, __getsm__, __gt__, __i__, __iadd__, __iand__, __idiv__, __ijsmod__, __ilshift__, __imatmul__, __imod__, __imul__, __in__, __init__, __ior__, __ipow__, __irshift__, __isub__, __ixor__, __jsUsePyNext__, __jsmod__, __k__, __kwargtrans__, __le__, __lshift__, __lt__, __matmul__, __mergefields__, __mergekwargtrans__, __mod__, __mul__, __ne__, __neg__, __nest__, __or__, __pow__, __pragma__, __proxy__, __pyUseJsNext__, __rshift__, __setitem__, __setproperty__, __setslice__, __sort__, __specialattrib__, __sub__, __super__, __t__, __terminal__, __truediv__, __withblock__, __xor__, all, any, assert, bool, bytearray, bytes, callable, chr, deepcopy, delattr, dict, dir, divmod, enumerate, getattr, hasattr, isinstance, issubclass, len, list, object, ord, print, property, py_TypeError, py_iter, py_metatype, py_next, py_reversed, py_typeof, range, repr, setattr, sorted, sum, tuple, zip} from './org.transcrypt.__runtime__.js';
import {ADD, ALT, ARROW, AUDIO, AUTO, AXES, BACKSPACE, BASELINE, BEVEL, BEZIER, BLEND, BLUR, BOLD, BOLDITALIC, BOTTOM, BURN, CENTER, CHORD, CLAMP, CLOSE, CONTROL, CORNER, CORNERS, CROSS, CURVE, DARKEST, DEGREES, DEG_TO_RAD, DELETE, DIFFERENCE, DILATE, DODGE, DOWN_ARROW, ENTER, ERODE, ESCAPE, EXCLUSION, FILL, GRAY, GRID, HALF_PI, HAND, HARD_LIGHT, HSB, HSL, IMAGE, IMMEDIATE, INVERT, ITALIC, LANDSCAPE, LEFT, LEFT_ARROW, LIGHTEST, LINEAR, LINES, LINE_LOOP, LINE_STRIP, MIRROR, MITER, MOVE, MULTIPLY, NEAREST, NORMAL, OPAQUE, OPEN, OPTION, OVERLAY, P2D, PI, PIE, POINTS, PORTRAIT, POSTERIZE, PROJECT, QUADRATIC, QUADS, QUAD_STRIP, QUARTER_PI, RADIANS, RADIUS, RAD_TO_DEG, REPEAT, REPLACE, RETURN, RGB, RIGHT, RIGHT_ARROW, ROUND, SCREEN, SHIFT, SOFT_LIGHT, SQUARE, STROKE, SUBTRACT, TAB, TAU, TEXT, TEXTURE, THRESHOLD, TOP, TRIANGLES, TRIANGLE_FAN, TRIANGLE_STRIP, TWO_PI, UP_ARROW, VIDEO, WAIT, WEBGL, _CTX_MIDDLE, _DEFAULT_FILL, _DEFAULT_LEADMULT, _DEFAULT_STROKE, _DEFAULT_TEXT_FILL, _P5_INSTANCE, abs, accelerationX, accelerationY, accelerationZ, acos, add_library, alpha, ambientLight, ambientMaterial, angleMode, append, applyMatrix, arc, arrayCopy, asin, atan, atan2, background, beginContour, beginShape, bezier, bezierDetail, bezierPoint, bezierTangent, bezierVertex, blend, blendMode, blue, boolean, box, brightness, byte, camera, ceil, changed, char, circle, color, colorMode, concat, cone, constrain, copy, cos, createA, createAudio, createButton, createCamera, createCanvas, createCapture, createCheckbox, createColorPicker, createDiv, createElement, createFileInput, createGraphics, createImage, createImg, createInput, createNumberDict, createP, createRadio, createSelect, createShader, createSlider, createSpan, createStringDict, createVector, createVideo, createWriter, cursor, curve, curveDetail, curvePoint, curveTangent, curveTightness, curveVertex, cylinder, day, debugMode, degrees, deviceOrientation, directionalLight, disableFriendlyErrors, displayDensity, displayHeight, displayWidth, dist, ellipse, ellipseMode, ellipsoid, endContour, endShape, exp, fill, filter, float, floor, focused, frameCount, frameRate, fullscreen, getURL, getURLParams, getURLPath, global_p5_injection, green, height, hex, hour, httpDo, httpGet, httpPost, hue, image, imageMode, input, int, join, key, keyCode, keyIsDown, keyIsPressed, lerp, lerpColor, lightness, lights, line, loadBytes, loadFont, loadImage, loadJSON, loadModel, loadPixels, loadShader, loadStrings, loadTable, loadXML, log, logOnloaded, loop, mag, map, match, matchAll, max, millis, min, minute, model, month, mouseButton, mouseIsPressed, mouseX, mouseY, nf, nfc, nfp, nfs, noCanvas, noCursor, noDebugMode, noFill, noLoop, noSmooth, noStroke, noTint, noise, noiseDetail, noiseSeed, norm, normalMaterial, orbitControl, ortho, pAccelerationX, pAccelerationY, pAccelerationZ, pRotationX, pRotationY, pRotationZ, perspective, pixelDensity, pixels, plane, pmouseX, pmouseY, point, pointLight, popMatrix, popStyle, pow, pre_draw, preload, push, pushMatrix, pushStyle, pwinMouseX, pwinMouseY, py_clear, py_get, py_pop, py_sort, py_split, quad, quadraticVertex, radians, random, randomGaussian, randomSeed, rect, rectMode, red, redraw, remove, removeElements, resetMatrix, resetShader, resizeCanvas, reverse, rotate, rotateX, rotateY, rotateZ, rotationX, rotationY, rotationZ, round, saturation, save, saveCanvas, saveFrames, saveJSON, saveStrings, saveTable, scale, second, select, selectAll, set, setAttributes, setCamera, setMoveThreshold, setShakeThreshold, shader, shearX, shearY, shininess, shorten, shuffle, sin, size, smooth, specularMaterial, sphere, splice, splitTokens, sq, sqrt, square, start_p5, str, stroke, strokeCap, strokeJoin, strokeWeight, subset, tan, text, textAlign, textAscent, textDescent, textFont, textLeading, textSize, textStyle, textWidth, texture, textureMode, textureWrap, tint, torus, touches, translate, triangle, trim, turnAxis, unchar, unhex, updatePixels, vertex, width, winMouseX, winMouseY, windowHeight, windowWidth, year} from './pyp5js.js';
var __name__ = 'sketch_010';
add_library ('p5.dom.js');
export var MY_POINTS = [tuple ([100, 50]), tuple ([300, 100]), tuple ([200, 300]), tuple ([100, 300])];
export var FRAME_IDX = 0;
export var POINT_SIZE = 10;
export var CNV = null;
export var setup = function () {
	if (arguments.length) {
		var __ilastarg0__ = arguments.length - 1;
		if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
			var __allkwargs0__ = arguments [__ilastarg0__--];
			for (var __attrib0__ in __allkwargs0__) {
			}
		}
	}
	else {
	}
	CNV = createCanvas (400, 400);
	var BUTTON_PREV = createButton ('Previous frame');
	BUTTON_PREV.position (CNV.position ().x, CNV.height + CNV.position ().y);
	BUTTON_PREV.mousePressed (prev_frame);
	var BUTTON_NEXT = createButton ('Next frame');
	BUTTON_NEXT.position (CNV.position ().x + BUTTON_PREV.size ().width, BUTTON_PREV.position ().y);
	BUTTON_NEXT.mousePressed (next_frame);
	background (190);
	draw_labels (MY_POINTS);
};
export var draw = function () {
	if (arguments.length) {
		var __ilastarg0__ = arguments.length - 1;
		if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
			var __allkwargs0__ = arguments [__ilastarg0__--];
			for (var __attrib0__ in __allkwargs0__) {
			}
		}
	}
	else {
	}
	background (190);
	draw_closed_curve_vertex (MY_POINTS, FRAME_IDX);
	draw_labels (MY_POINTS);
};
export var mouseClicked = function () {
	if (arguments.length) {
		var __ilastarg0__ = arguments.length - 1;
		if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
			var __allkwargs0__ = arguments [__ilastarg0__--];
			for (var __attrib0__ in __allkwargs0__) {
			}
		}
	}
	else {
	}
	if (is_point_in_canvas (mouseX, mouseY)) {
		var i = get_point_index (mouseX, mouseY);
		if (i != null) {
			MY_POINTS.py_pop (i);
			if (FRAME_IDX >= len (MY_POINTS)) {
				FRAME_IDX = len (MY_POINTS) - 1;
			}
		}
		else {
			MY_POINTS.append (tuple ([mouseX, mouseY]));
		}
	}
};
export var get_point_index = function (x, y) {
	if (arguments.length) {
		var __ilastarg0__ = arguments.length - 1;
		if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
			var __allkwargs0__ = arguments [__ilastarg0__--];
			for (var __attrib0__ in __allkwargs0__) {
				switch (__attrib0__) {
					case 'x': var x = __allkwargs0__ [__attrib0__]; break;
					case 'y': var y = __allkwargs0__ [__attrib0__]; break;
				}
			}
		}
	}
	else {
	}
	for (var [idx, [p_x, p_y]] of enumerate (MY_POINTS)) {
		if ((p_x - POINT_SIZE < x && x < p_x + POINT_SIZE) && (p_y - POINT_SIZE < y && y < p_y + POINT_SIZE)) {
			return idx;
		}
	}
};
export var is_point_in_canvas = function (x, y) {
	if (arguments.length) {
		var __ilastarg0__ = arguments.length - 1;
		if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
			var __allkwargs0__ = arguments [__ilastarg0__--];
			for (var __attrib0__ in __allkwargs0__) {
				switch (__attrib0__) {
					case 'x': var x = __allkwargs0__ [__attrib0__]; break;
					case 'y': var y = __allkwargs0__ [__attrib0__]; break;
				}
			}
		}
	}
	else {
	}
	if ((x < 0 || x > CNV.width) || (y < 0 || y > CNV.height)) {
		return false;
	}
	return true;
};
export var next_frame = function () {
	if (arguments.length) {
		var __ilastarg0__ = arguments.length - 1;
		if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
			var __allkwargs0__ = arguments [__ilastarg0__--];
			for (var __attrib0__ in __allkwargs0__) {
			}
		}
	}
	else {
	}
	if (FRAME_IDX < len (MY_POINTS) - 1) {
		FRAME_IDX++;
	}
};
export var prev_frame = function () {
	if (arguments.length) {
		var __ilastarg0__ = arguments.length - 1;
		if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
			var __allkwargs0__ = arguments [__ilastarg0__--];
			for (var __attrib0__ in __allkwargs0__) {
			}
		}
	}
	else {
	}
	if (FRAME_IDX > 0) {
		FRAME_IDX--;
	}
};
export var draw_closed_curve_vertex = function (points, max_idx) {
	if (arguments.length) {
		var __ilastarg0__ = arguments.length - 1;
		if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
			var __allkwargs0__ = arguments [__ilastarg0__--];
			for (var __attrib0__ in __allkwargs0__) {
				switch (__attrib0__) {
					case 'points': var points = __allkwargs0__ [__attrib0__]; break;
					case 'max_idx': var max_idx = __allkwargs0__ [__attrib0__]; break;
				}
			}
		}
	}
	else {
	}
	if (len (points) < 2) {
		return ;
	}
	var used_points = [];
	beginShape ();
	var idx = len (points) - 1;
	curveVertex (...points [idx]);
	used_points.append (idx);
	for (var [idx, p] of enumerate (points)) {
		if (idx > max_idx) {
			break;
		}
		curveVertex (...p);
		used_points.append (idx);
	}
	var idx = 0;
	curveVertex (...points [idx]);
	used_points.append (idx);
	var idx = 1;
	curveVertex (...points [idx]);
	used_points.append (idx);
	endShape ();
	textSize (10);
	noStroke ();
	text ('Points used to draw this curve (first and last are control points only)', 5, CNV.height - 30);
	textSize (20);
	text (', '.join (used_points), 10, CNV.height - 10);
	stroke (0);
	for (var i = 0; i < len (used_points) - 1; i++) {
		draw_dotted_line (points [used_points [i]], points [used_points [i + 1]]);
	}
};
export var draw_labels = function (points) {
	if (arguments.length) {
		var __ilastarg0__ = arguments.length - 1;
		if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
			var __allkwargs0__ = arguments [__ilastarg0__--];
			for (var __attrib0__ in __allkwargs0__) {
				switch (__attrib0__) {
					case 'points': var points = __allkwargs0__ [__attrib0__]; break;
				}
			}
		}
	}
	else {
	}
	strokeWeight (POINT_SIZE);
	for (var [idx, p] of enumerate (points)) {
		var ts = 32;
		textSize (ts);
		var textY = p [1] - ts / 2;
		if (p [1] > CNV.height / 2) {
			var textY = p [1] + ts;
		}
		noStroke ();
		text (idx, p [0], textY);
		stroke (0);
		point (...p);
	}
	strokeWeight (1);
};
export var draw_dotted_line = function (p1, p2) {
	if (arguments.length) {
		var __ilastarg0__ = arguments.length - 1;
		if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
			var __allkwargs0__ = arguments [__ilastarg0__--];
			for (var __attrib0__ in __allkwargs0__) {
				switch (__attrib0__) {
					case 'p1': var p1 = __allkwargs0__ [__attrib0__]; break;
					case 'p2': var p2 = __allkwargs0__ [__attrib0__]; break;
				}
			}
		}
	}
	else {
	}
	stroke (100);
	strokeWeight (3);
	for (var i = 0; i < 11; i++) {
		var x = lerp (p1 [0], p2 [0], i / 10);
		var y = lerp (p1 [1], p2 [1], i / 10);
		point (x, y);
	}
	stroke (0);
	strokeWeight (1);
};

//# sourceMappingURL=sketch_010.map