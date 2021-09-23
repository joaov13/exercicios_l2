/*
  ____                    _      _          _
 / ___|___  ___ _ __ ___ (_) ___| |    __ _| |__  ___
| |   / _ \/ __| '_ ` _ \| |/ __| |   / _` | '_ \/ __|
| |__| (_) \__ \ | | | | | | (__| |__| (_| | |_) \__ \
 \____\___/|___/_| |_| |_|_|\___|_____\__,_|_.__/|___/


Hue - Responsive Under Construction Template
Version 1.1.4 - Last updated April 2016
Copyright 2016 CosmicLabs

This template and more are available to purchase on Themeforest.net
http://themeforest.net/user/cosmiclabs/portfolio

For template support, see the documentation files or get in touch with us.
Support site: http://cosmiclabs.co.uk/support
Support email: support@cosmiclabs.co.uk

*/

// ************************************************************* //
// SETTINGS for Hue Responsive Under Construction Template
// ************************************************************* //


// To setup, change the variables below
// Follow instructions in comments, see documentation for more detail

// ==== COLOUR SCHEME ====
// Type in the HEX Code for the colour you want to use as the background of the site
// Remember to include the Hex (#) symbol, e.g. #2c3e50
// Need some colours to choose from? Nice choice of Flat UI colours here: http://flatuicolors.com
// Darker colours work best - avoid light / pale colours
// Set opacity of colour overlay, between 0 and 1

var colour = "#5cca47";
var bgOpacityLevel = "0.80";


// ==== SLIDESHOW BACKGROUND ====
// Set URLs to background images inside the array
// Each image must be on its own line, inbetween speech marks (" ") and with a comma at the end of the line
// Add / remove images by changing the number of lines below
// Variable slideshowFade = transition speed for fade animation, in milliseconds
// Variable slideshowDuration = time each slide is shown for, in milliseconds

var slideshowBackground = 'on';

var slideshowBackgroundURLS = [
	"images/background1.jpg",
	"images/background2.jpg",
	"images/background4.jpg",
];

var slideshowFade = 1000;
var slideshowDuration = 4000;


// ==== VIDEO BACKGROUND ====
// Enable Video Background - 'on' to enable, 'off' to disable
// Cannot work on mobile devices due to device restrictions, instead shows slideshow
// If disabled slideshow is shown
// Paste YouTube URL into the videoBackgronudURL variable - use YouTube link NOT embed code
// Set videoMuted to 'true' and background videos will be muted with no toggle mute button visible
// Set videoMuted to 'false' and videos will not be muted, and the toggle mute button will be visible on the site so users can turn off audio if they want

var videoBackground = 'off';
var videoBackgroundURL = 'PASTE-YOUTUBE-URL-HERE';
var videoMuted = true;


// ==== COUNTDOWN ====
// Set up the date and time that will be counted down to
// Enter date in the format (24 hr clock): DD Month YYYY HH:MM:SS for example: 01 January 2015 23:04:00

var countdownDate = "28 February 2021 00:00:00";