class ShapeFactory:
    def __init__(self):
        noStroke()
        self.buildBasicPlayer()
        self.buildBasicEnemy()
        self.buildEnemyTwo()
        self.buildEnemyThree()
        
    def buildBasicBullet(self):
        self.basicBulletRadius = 20;
        basicBullet = createShape(ELLIPSE, -10, -10, 20, 20);
        basicBullet.setStroke(color(255));
        basicBullet.setStrokeWeight(4);
        basicBullet.setFill(color(127));
        self.basicBullet = basicBullet
    
    def buildBasicPlayer(self):
        self.basicPlayerRadius = 30
        basicPlayer = createShape(GROUP)
        chassis = createShape()
        chassis.beginShape();
        chassis.noStroke();
        chassis.fill(125);
        chassis.strokeWeight(2);
        chassis.vertex(0, -100);
        chassis.vertex(10, -80);
        chassis.vertex(10, -60);
        chassis.vertex(20, 0);
        chassis.vertex(40, -40);
        chassis.vertex(40, 0);
        chassis.vertex(20, 40);
        chassis.vertex(-20, 40);
        chassis.vertex(-40, 0);
        chassis.vertex(-40, -40);
        chassis.vertex(-20, 0);
        chassis.vertex(-10, -60);
        chassis.vertex(-10, -80);
        chassis.vertex(0, -100);
        chassis.endShape();
        fill(255, 255, 0);
        leftOrb = createShape(ELLIPSE, -50, -50, 20, 20);
        rightOrb = createShape(ELLIPSE, 30, -50, 20, 20);
        fill(102, 255, 255);
        cockpit = createShape(ELLIPSE, -10, -25, 20, 50);
        basicPlayer.addChild(chassis);
        basicPlayer.addChild(leftOrb);
        basicPlayer.addChild(rightOrb);
        basicPlayer.addChild(cockpit);
        basicPlayer.scale(0.55);
        self.basicPlayer = basicPlayer
        
    def buildBasicEnemy(self):
        self.basicEnemyRadius = 40;
        basicEnemy = createShape();
        basicEnemy.beginShape();
        basicEnemy.noStroke();
        basicEnemy.strokeWeight(5);
        basicEnemy.vertex(-20, 30);
        basicEnemy.vertex(20, 30);
        basicEnemy.vertex(20, 20);
        basicEnemy.vertex(40, 0);
        basicEnemy.vertex(40, -20);
        basicEnemy.vertex(30, -30);
        basicEnemy.vertex(20, -30);
        basicEnemy.vertex(20, 0);
        basicEnemy.vertex(10, 0);
        basicEnemy.vertex(0, -10);
        basicEnemy.vertex(-10, 0);
        basicEnemy.vertex(-20, 0);
        basicEnemy.vertex(-20, -30);
        basicEnemy.vertex(-30, -30);
        basicEnemy.vertex(-40, -20);
        basicEnemy.vertex(-40, 0);
        basicEnemy.vertex(-20, 20);
        basicEnemy.vertex(-20, 30);
        basicEnemy.endShape();
        basicEnemy.rotate(PI);
        basicEnemy.scale(.5);
        self.basicEnemy = basicEnemy
    
    def buildEnemyTwo(self):
        enemyTwo = createShape(GROUP);
        fill(115, 20, 240); #purple
        chassis = createShape(ELLIPSE, -90, -40, 180, 80);
        fill(20, 200, 255); #light blue
        dome1 = createShape(ARC, -50, -15, 100, 30, 0, PI);
        dome2 = createShape(ARC, -50, -50, 100, 100, PI, TWO_PI);
        enemyTwo.addChild(chassis);
        enemyTwo.addChild(dome1);
        enemyTwo.addChild(dome2);
        enemyTwo.scale(.3);
        self.enemyTwo = enemyTwo
        
    def buildEnemyThree(self):
        enemyThree = createShape(GROUP);
        fill(245, 12, 82); #more of a red
        chassis = createShape(ELLIPSE, -90, -40, 180, 80);
        fill(245, 207, 12); #light blue
        dome1 = createShape(ARC, -50, -15, 100, 30, 0, PI);
        dome2 = createShape(ARC, -50, -50, 100, 100, PI, TWO_PI);
        enemyThree.addChild(chassis);
        enemyThree.addChild(dome1);
        enemyThree.addChild(dome2);
        enemyThree.scale(.3);
        self.enemyThree = enemyThree
        