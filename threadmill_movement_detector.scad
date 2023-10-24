//////////////////////////
//
//
// CC BY SA 4.0 
// Andre M Chagas
// 20/06/2023
///////////////////////////



tol = 0.2;



$fn=60;


//gear fit information
fitX=1.7;
fitY=4.6;
fitZ=10;
fitDispla=1.5;





wheelD=30;
holeD = 3.5;
pi=3.142;

module axis_fit(){

    difference(){
        translate([0,0,0]){
            cylinder(d=8,h=fitZ);
        }//end translate
        translate([0,0,(fitZ/2)+1]){
            cube([fitX+2*tol,fitY+2*tol,fitZ],center=true);
            rotate([0,0,90]){
                cube([fitX+2*tol,4.71+2*tol,fitZ],center=true);
                }//end rotate
        }//end translate
        }//end difference

    
}//end module

axis_fit();

difference(){
cylinder(h=2,d=wheelD);

for (i = [0:45:360]){
    translate([sin(i)*(wheelD-holeD-1.5)/2,cos(i)*(wheelD-holeD-1.5)/2,-5]){
        cylinder(d=holeD,h=20);
    }//end translate
    }//end for
    
}


//uses a gear library:
//https://github.com/chrisspen/gears

//use <gears/gears.scad>

//thorlabs pole which holds the system in position
//poleDia = 12.9;
//poleHei = 25;

//servo motor dimensions
//servoX = 16;
//servoY = 24;
//servoZ = 25.6;
//servoPocketH = 9;

//wall thickness of the servo holder
//holderWall = 2;



//rotatorDia = 68;
//rotatorHei = 8;


//information about nut and screws that are used to fix things
//screwDia=3.95;

//nutDia = 6.91;
//nutHei = 3.25;

//gear and rail information
//gearModule = 1;
//nTeeth = 25;
//gearW = 10;
//centralBoreD = 5;
//pressureAngle = 30;
//helixAngle = 10;
//railL = 30;
//railH=5;
