// Transcrypt'ed from Python, 2019-05-05 14:12:06
import {AssertionError, AttributeError, BaseException, DeprecationWarning, Exception, IndexError, IterableError, KeyError, NotImplementedError, RuntimeWarning, StopIteration, UserWarning, ValueError, Warning, __JsIterator__, __PyIterator__, __Terminal__, __add__, __and__, __call__, __class__, __envir__, __eq__, __floordiv__, __ge__, __get__, __getcm__, __getitem__, __getslice__, __getsm__, __gt__, __i__, __iadd__, __iand__, __idiv__, __ijsmod__, __ilshift__, __imatmul__, __imod__, __imul__, __in__, __init__, __ior__, __ipow__, __irshift__, __isub__, __ixor__, __jsUsePyNext__, __jsmod__, __k__, __kwargtrans__, __le__, __lshift__, __lt__, __matmul__, __mergefields__, __mergekwargtrans__, __mod__, __mul__, __ne__, __neg__, __nest__, __or__, __pow__, __pragma__, __proxy__, __pyUseJsNext__, __rshift__, __setitem__, __setproperty__, __setslice__, __sort__, __specialattrib__, __sub__, __super__, __t__, __terminal__, __truediv__, __withblock__, __xor__, all, any, assert, bool, bytearray, bytes, callable, chr, deepcopy, delattr, dict, dir, divmod, enumerate, getattr, hasattr, input, isinstance, issubclass, len, list, object, ord, property, py_TypeError, py_iter, py_metatype, py_next, py_reversed, py_typeof, range, repr, setattr, sorted, sum, tuple, zip} from './org.transcrypt.__runtime__.js';
import {BOTTOM, CENTER, CLOSE, CMYK, DEGREES, HALF_PI, HSB, LEFT, PI, QUARTER_PI, RADIANS, RGB, RIGHT, SHIFT, TAU, TOP, TWO_PI, WEBGL, _P5_INSTANCE, abs, accelerationX, accelerationY, accelerationZ, acos, alpha, ambientLight, ambientMaterial, angleMode, append, applyMatrix, arc, arrayCopy, asin, atan, atan2, background, beginContour, beginShape, bezier, bezierDetail, bezierPoint, bezierTangent, bezierVertex, blend, blendMode, blue, boolean, box, brightness, byte, camera, ceil, char, circle, color, colorMode, concat, cone, constrain, copy, cos, createCamera, createCanvas, createGraphics, createImage, createNumberDict, createShader, createStringDict, createVector, createWriter, cursor, curve, curveDetail, curvePoint, curveTangent, curveTightness, curveVertex, cylinder, day, debugMode, degrees, deviceMoved, deviceOrientation, deviceShaken, deviceTurned, directionalLight, disableFriendlyErrors, displayDensity, displayHeight, displayWidth, dist, doubleClicked, ellipse, ellipseMode, ellipsoid, endContour, endShape, exp, fill, filter, float, floor, focused, frameCount, frameRate, fullscreen, getURL, getURLParams, getURLPath, global_p5_injection, green, height, hex, hour, httpDo, httpGet, httpPost, hue, image, imageMode, int, join, key, keyCode, keyIsDown, keyIsPressed, keyPressed, keyReleased, keyTyped, lerp, lerpColor, lightness, lights, line, loadBytes, loadFont, loadImage, loadJSON, loadModel, loadPixels, loadShader, loadStrings, loadTable, loadXML, log, loop, mag, map, match, matchAll, max, millis, min, minute, model, month, mouseButton, mouseClicked, mouseDragged, mouseIsPressed, mouseMoved, mousePressed, mouseReleased, mouseWheel, mouseX, mouseY, nf, nfc, nfp, nfs, noCanvas, noCursor, noDebugMode, noFill, noLoop, noSmooth, noStroke, noTint, noise, noiseDetail, noiseSeed, norm, normalMaterial, orbitControl, ortho, pAccelerationX, pAccelerationY, pAccelerationZ, pRotationX, pRotationY, pRotationZ, perspective, pixelDensity, pixels, plane, pmouseX, pmouseY, point, pointLight, pow, pre_draw, preload, print, push, pwinMouseX, pwinMouseY, py_clear, py_get, py_pop, py_sort, py_split, quad, quadraticVertex, radians, random, randomGaussian, randomSeed, rect, rectMode, red, redraw, remove, resetMatrix, resetShader, resizeCanvas, reverse, rotate, rotateX, rotateY, rotateZ, rotationX, rotationY, rotationZ, round, saturation, save, saveCanvas, saveFrames, saveJSON, saveStrings, saveTable, scale, second, set, setAttributes, setCamera, setMoveThreshold, setShakeThreshold, shader, shearX, shearY, shininess, shorten, shuffle, sin, smooth, specularMaterial, sphere, splice, splitTokens, sq, sqrt, square, start_p5, str, stroke, strokeCap, strokeJoin, strokeWeight, subset, tan, text, textAlign, textAscent, textDescent, textFont, textLeading, textSize, textStyle, textWidth, texture, textureMode, textureWrap, tint, torus, touchEnded, touchMoved, touchStarted, touches, translate, triangle, trim, turnAxis, unchar, unhex, updatePixels, vertex, width, winMouseX, winMouseY, windowHeight, windowResized, windowWidth, year} from './pytop5js.js';
var __name__ = '__main__';
export var boids = list ([]);
export var setup = function () {
	createCanvas (720, 400);
	for (var i = 0; i < 40; i++) {
		boids.append (Boid (random (720), random (400)));
	}
};
export var draw = function () {
	background (51);
	for (var boid of boids) {
		boid.run (boids);
	}
};
export var Boid =  __class__ ('Boid', [object], {
	__module__: __name__,
	get __init__ () {return __get__ (this, function (self, x, y) {
		self.acceleration = createVector (0, 0);
		self.velocity = p5.Vector.random2D ();
		self.position = createVector (x, y);
		self.r = 3.0;
		self.maxspeed = 3;
		self.maxforce = 0.05;
	});},
	get run () {return __get__ (this, function (self, boids) {
		self.flock (boids);
		self.py_update ();
		self.borders ();
		self.render ();
	});},
	get applyForce () {return __get__ (this, function (self, force) {
		self.acceleration.add (force);
	});},
	get flock () {return __get__ (this, function (self, boids) {
		var sep = self.separate (boids);
		var ali = self.align (boids);
		var coh = self.cohesion (boids);
		sep.mult (2.5);
		ali.mult (1.0);
		coh.mult (1.0);
		self.applyForce (sep);
		self.applyForce (ali);
		self.applyForce (coh);
	});},
	get py_update () {return __get__ (this, function (self) {
		self.velocity.add (self.acceleration);
		self.velocity.limit (self.maxspeed);
		self.position.add (self.velocity);
		self.acceleration.mult (0);
	});},
	get seek () {return __get__ (this, function (self, target) {
		var desired = p5.Vector.sub (target, self.position);
		desired.normalize ();
		desired.mult (self.maxspeed);
		var steer = p5.Vector.sub (desired, self.velocity);
		steer.limit (self.maxforce);
		return steer;
	});},
	get render () {return __get__ (this, function (self) {
		fill (127, 127);
		stroke (200);
		ellipse (self.position.x, self.position.y, 16, 16);
	});},
	get borders () {return __get__ (this, function (self) {
		if (self.position.x < -(self.r)) {
			self.position.x = width + self.r;
		}
		if (self.position.y < -(self.r)) {
			self.position.y = height + self.r;
		}
		if (self.position.x > width + self.r) {
			self.position.x = -(self.r);
		}
		if (self.position.y > height + self.r) {
			self.position.y = -(self.r);
		}
	});},
	get separate () {return __get__ (this, function (self, boids) {
		var desiredseparation = 25.0;
		var steer = createVector (0, 0);
		var count = 0;
		for (var i = 0; i < len (boids); i++) {
			var d = p5.Vector.dist (self.position, boids [i].position);
			if (d > 0 && d < desiredseparation) {
				var diff = p5.Vector.sub (self.position, boids [i].position);
				diff.normalize ();
				diff.div (d);
				steer.add (diff);
				count++;
			}
		}
		if (count > 0) {
			steer.div (count);
		}
		if (steer.mag () > 0) {
			steer.normalize ();
			steer.mult (self.maxspeed);
			steer.sub (self.velocity);
			steer.limit (self.maxforce);
		}
		return steer;
	});},
	get align () {return __get__ (this, function (self, boids) {
		var neighbordist = 50;
		var sum = createVector (0, 0);
		var count = 0;
		for (var i = 0; i < len (boids); i++) {
			var d = p5.Vector.dist (self.position, boids [i].position);
			if (d > 0 && d < neighbordist) {
				sum.add (boids [i].velocity);
				count++;
			}
		}
		if (count > 0) {
			sum.div (count);
			sum.normalize ();
			sum.mult (self.maxspeed);
			var steer = p5.Vector.sub (sum, self.velocity);
			steer.limit (self.maxforce);
			return steer;
		}
		else {
			return createVector (0, 0);
		}
	});},
	get cohesion () {return __get__ (this, function (self, boids) {
		var neighbordist = 50;
		var sum = createVector (0, 0);
		var count = 0;
		for (var i = 0; i < len (boids); i++) {
			var d = p5.Vector.dist (self.position, boids [i].position);
			if (d > 0 && d < neighbordist) {
				sum.add (boids [i].position);
				count++;
			}
		}
		if (count > 0) {
			sum.div (count);
			return self.seek (sum);
		}
		else {
			return createVector (0, 0);
		}
	});}
});
start_p5 (setup, draw);

//# sourceMappingURL=sketch_004.map