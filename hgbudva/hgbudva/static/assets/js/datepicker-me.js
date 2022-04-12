( function( factory ) {
	if ( typeof define === "function" && define.amd ) {

		// AMD. Register as an anonymous module.
		define( [ "../widgets/datepicker" ], factory );
	} else {

		// Browser globals
		factory( jQuery.datepicker );
	}
}( function( datepicker ) {

datepicker.regional[ "me" ] = {
	closeText: "Zatvori",
	prevText: "&#x3C;",
	nextText: "&#x3E;",
	currentText: "Danas",
	monthNames: [ "Januar","Februar","Mart","April","Maj","Jun",
	"Jul","Avgust","Septembar","Oktobar","Novembar","Decembar" ],
	monthNamesShort: [ "Jan","Feb","Mar","Apr","Maj","Jun",
	"Jul","Avg","Sep","Okt","Nov","Dec" ],
	dayNames: [ "Neđelja","Poneđeljak","Utorak","Srijeda","Četvrtak","Petak","Subota" ],
	dayNamesShort: [ "Ned","Pon","Uto","Sre","Čet","Pet","Sub" ],
	dayNamesMin: [ "Ne","Po","Ut","Sr","Če","Pe","Su" ],
	weekHeader: "Sed",
	dateFormat: "dd.mm.yy",
	firstDay: 1,
	isRTL: false,
	showMonthAfterYear: false,
	yearSuffix: "" };
datepicker.setDefaults( datepicker.regional[ "me" ] );

return datepicker.regional[ "me" ];

} ) );