

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
keypress_one_up = False
keypress_one_down = False
keypress_two_up = False
keypress_two_down = False

WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80

HALF_PAD_WIDTH = PAD_WIDTH  2
HALF_PAD_HEIGHT = PAD_HEIGHT  2
paddle1_vel = 0
paddle2_vel = 0

velocity = 4
score1 = 0
score2 = 0

# helper function that spawns a ball, returns a position vector and a velocity vector
# if right is True, spawn to the right, else spawn to the left
def ball_init(right)
    global ball_pos, ball_vel, score1, score2, winner # these are vectors stored as lists
    ball_pos = [300, 200]
    if score1 == 7
        ball_vel = [0,0]
    elif score2 == 7
        ball_vel = [0,0]
    else
        if right
            ball_vel = [-random.randrange(3, 4), -random.randrange(1, 6)]
        elif not right
            ball_vel = [random.randrange(3, 4), -random.randrange(1, 6)]

# define event handlers
def init()
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are floats
    global score1, score2
    paddle1_pos = HEIGHT  2 - HALF_PAD_HEIGHT
    paddle2_pos = HEIGHT  2 - HALF_PAD_HEIGHT
    right = True
    ball_init(right)

def restart()
    global score1, score2
    score1 = 0
    score2 = 0
    init()

def draw(canvas)
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel, winner
 
    # update paddle's vertical position, keep paddle on the screen
    #canvas.draw_polygon([[200, 60], [300, 60], [400, 20], [400, 40]], 2, 'Red')
    canvas.draw_text(str(score1) + '      ' + str(score2), (230,68), 50, White)
    canvas.draw_text(str(Player 1) +      + str(Player 2), (205,30), 25, White)
    
    
    if paddle1_pos + paddle1_vel = 0
        if paddle1_pos + paddle1_vel = HEIGHT - PAD_HEIGHT
            paddle1_pos += paddle1_vel
    if paddle2_pos + paddle2_vel = 0
        if paddle2_pos + paddle2_vel = HEIGHT - PAD_HEIGHT
            paddle2_pos += paddle2_vel
    
    # draw mid line and gutters
    
    canvas.draw_line([WIDTH  2, 0],[WIDTH  2, HEIGHT], 1, White)
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, White)
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, White)
   
    paddle1 = canvas.draw_line([HALF_PAD_WIDTH, paddle2_pos], [HALF_PAD_WIDTH, paddle2_pos + PAD_HEIGHT], PAD_WIDTH, White)
    paddle2 = canvas.draw_line([WIDTH - HALF_PAD_WIDTH, paddle1_pos], [WIDTH - HALF_PAD_WIDTH, paddle1_pos + PAD_HEIGHT], PAD_WIDTH, White)
    
    # update ball
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]
    if ball_pos[1]  2BALL_RADIUS
        ball_vel[1] = -ball_vel[1]
    if ball_pos[1]  HEIGHT - 2BALL_RADIUS
        ball_vel[1] = -ball_vel[1]
    if ball_pos[0] - BALL_RADIUS  PAD_WIDTH
        if ball_pos[1] in range(paddle2_pos,paddle2_pos + PAD_HEIGHT + BALL_RADIUS)
            ball_vel[0] = 1.1-ball_vel[0]
        else
            score2 += 1
            right = False
            ball_init(right)
    if ball_pos[0] + BALL_RADIUS  WIDTH - PAD_WIDTH
        if ball_pos[1] in range(paddle1_pos,paddle1_pos + PAD_HEIGHT + BALL_RADIUS)
            ball_vel[0] = 1.1-ball_vel[0]
        else
            score1 += 1
            right = True
            ball_init(right)
    
    # draw ball and scores
    ball = canvas.draw_circle(ball_pos, BALL_RADIUS, 5, Blue, White)

    # draw winner
    if score1 == 7
        canvas.draw_text('PLAYER 1 WON!!!!!', (200,140), 20, White)
    if score2 == 7
        canvas.draw_text('PLAYER 2 WON!!!!!', (200,140), 20, White)
        
def keydown(key)
    global paddle1_vel, paddle2_vel, keypress_one_up, keypress_one_down, keypress_two_down, keypress_two_up, velocity
    if key == simplegui.KEY_MAP[up]
        paddle1_vel = -velocity
        keypress_one_up = True
    if key == simplegui.KEY_MAP[down]
        paddle1_vel = velocity
        keypress_one_down = True
    if key == simplegui.KEY_MAP[w]
        paddle2_vel = -velocity
        keypress_two_up = True
    if key == simplegui.KEY_MAP[s]
        paddle2_vel = velocity
        keypress_two_down = True
    
   
def keyup(key)
    global paddle1_vel, paddle2_vel, keypress_one_up, keypress_one_down, keypress_two_down, keypress_two_up
    if key == simplegui.KEY_MAP[up]
        keypress_one_up = False
        if not keypress_one_down
            paddle1_vel = 0
    if key == simplegui.KEY_MAP[down]
        keypress_one_down = False
        if not keypress_one_up
            paddle1_vel = 0
    if key == simplegui.KEY_MAP[w]
        keypress_two_up = False
        if not keypress_two_down
            paddle2_vel = 0
    if key == simplegui.KEY_MAP[s]
        keypress_two_down = False
        if not keypress_two_up
            paddle2_vel = 0


# create frame
frame = simplegui.create_frame(Pong, WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button(Restart, restart, 100)


# start frame
init()
frame.start()
