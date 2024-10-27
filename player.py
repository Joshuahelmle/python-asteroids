import pygame
from circleshape import CircleShape
from constants import PLAYER_RADIUS, PLAYER_SHOOT_COOLDOWN, PLAYER_SHOOT_SPEED, PLAYER_SPEED, PLAYER_TURN_SPEED
from shot import Shot

# Player class
class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.shoot_cooldown = 0


    def triangle(self) -> list[pygame.Vector2]:
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        pygame.draw.polygon(screen, (255, 255, 255), self.triangle(), 2)
    
    def rotate(self, delta):
        self.rotation += delta * PLAYER_TURN_SPEED
    
    def update(self, delta):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.rotate(-delta)
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.rotate(delta)
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.move(delta)
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.move(-delta)
        if keys[pygame.K_SPACE] and self.shoot_cooldown <= 0:
            self.shoot()
        if self.shoot_cooldown > 0:
            self.shoot_cooldown -= delta
            if self.shoot_cooldown < 0:
                self.shoot_cooldown = 0
        
    def move(self, delta):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * delta * PLAYER_SPEED

    def shoot(self):
        shot = Shot(self.position.x, self.position.y, 5)
        shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
        self.shoot_cooldown = PLAYER_SHOOT_COOLDOWN 