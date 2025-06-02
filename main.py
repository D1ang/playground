import pygame
import math


class Camera:
    def __init__(self, position, angle, max_distance, max_angle):
        self.postition = position
        self.angle = angle
        self.max_distance = max_distance
        self.max_angle = max_angle

        self.stand = pygame.image.load("sprites/stand.png").convert_alpha()  # Load stand image
        self.camera = pygame.image.load("sprites/camera.png").convert_alpha()  # Load camera image

    def draw(self, screen):
        """Draw the camera and its stand on the screen."""
        self.pov_cone(screen)  # Draw the point of view cone

        screen.blit(self.stand, self.stand.get_rect(center=self.postition))
        rotate_camera = pygame.transform.rotate(self.camera, self.angle)  # Rotate the camera image
        screen.blit(rotate_camera, rotate_camera.get_rect(center=self.postition))  # Draw the rotated camera image

    def pov_cone(self, screen):
        """Draw the point of view cone."""
        cone_surface = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)

        start_angle = self.angle - self.max_angle / 2
        stop_angle = self.angle + self.max_angle / 2

        points = [self.postition]

        for angle in range(math.floor(start_angle), math.ceil(stop_angle)):
            vector = pygame.Vector2.from_polar((self.max_distance, -angle))
            points.append(self.postition + vector)

        pygame.draw.polygon(cone_surface, (255, 0, 0, 50), points)  # Draw the cone with a semi-transparent red color

        screen.blit(cone_surface, (0, 0))  # Draw the cone surface on the screen

    def detect_player(self):
        player = player_position - self.postition  # Vector from camera to player

        # Check if the player is within the camera's point of view cone
        if player.length() > self.max_distance:
            return False

        camera_direction = pygame.Vector2(math.cos(math.radians(self.angle)), -math.sin(math.radians(self.angle)))

        # Calculate the angle between the camera direction and the player vector
        angle_difference = camera_direction.angle_to(player)

        if abs(angle_difference) > 180:
            angle_difference = abs(angle_difference) - 360

        if abs(angle_difference) > self.max_angle / 2:
            return False

        # Check if an obstacle is blocking the view
        for _, rect in obstacles:
            if rect.clipline(self.postition, player_position):
                return False

        return True  # Player is detected if all checks pass

    def update_rotation(self):
        """Update the camera's rotation based on player position."""
        if self.detect_player():
            direction = player_position - self.postition
            self.angle = -math.degrees(math.atan2(direction.y, direction.x))


pygame.init()
WIDTH, HEIGHT = 1280, 720
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
FPS = 60

player = pygame.image.load("sprites/player.png").convert_alpha()  # Load player image
player_position = pygame.Vector2(WIDTH // 2, HEIGHT // 2)  # Start in the center of the screen
player_rotation = 0  # Initial rotation angle

obstacles = []  # List to hold obstacles

camera_1 = Camera(position=(200, 200), angle=0, max_distance=250, max_angle=90)  # Initialize camera
camera_2 = Camera(position=(800, 500), angle=0, max_distance=250, max_angle=90)  # Initialize camera


def obstacle(pos):
    image = pygame.image.load("sprites/crate.png").convert_alpha()  # Load obstacle image
    rect = image.get_rect(center=pos)  # Get the rect for the image
    obstacles.append((image, rect))  # Append the image and its rect to the obstacles list


def player_movements():
    """Returns the current position of the player."""
    speed = 3.5  # Speed of the player
    keys = pygame.key.get_pressed()
    direction = pygame.Vector2(keys[pygame.K_RIGHT] - keys[pygame.K_LEFT], keys[pygame.K_DOWN] - keys[pygame.K_UP])

    if direction.length() > 0:
        new_position = player_position + direction.normalize() * speed
        new_rotation = -math.degrees(math.atan2(direction.y, direction.x))  # Calculate rotation angle

        return new_position, new_rotation

    return player_position, player_rotation


# ----------------------------------- Main game loop ----------------------------------- #

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            obstacle(event.pos)  # Create an obstacle at the mouse click position

    player_position, player_rotation = player_movements()  # Update player position and rotation

    camera_1.update_rotation()  # Update camera rotation based on player position
    camera_2.update_rotation()  # Update camera rotation based on player position


    screen.fill((0, 0, 0))  # Clear the screen with black

    camera_1.draw(screen)  # Draw the camera and its stand
    camera_2.draw(screen)  # Draw the camera and its stand


    screen.blits(obstacles)  # Draw all obstacles

    rotated_player = pygame.transform.rotate(player, player_rotation)  # Rotate the player image
    rotated_rect = rotated_player.get_rect(center=player_position)  # Get the rect for the rotated image
    screen.blit(rotated_player, rotated_rect)  # Draw the rotated player image

    pygame.display.flip()  # Update the display
    clock.tick(FPS)  # Maintain the frame rate

pygame.quit()  # Clean up and close the window
