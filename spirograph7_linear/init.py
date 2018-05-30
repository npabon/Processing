from support import Gimbal, Gimbal_Hinge, Hinge_Hinge, Linear_Traj

def get_traj():
    
    #################### GIMBAL HINGE 1 #########################
    # gimbal 1
    g1_pos = PVector(200, 0)
    g1_amp = PVector(random(40, 90),random(40, 90))
    g1_angle = random(TWO_PI) 
    g1_speed = random(.0495,.0505) 
    g1_damp = 1.0
    g1 = Gimbal(g1_pos, g1_amp, angle=g1_angle, speed=g1_speed, damp=g1_damp)
    # gimbal 2
    g2_pos = PVector(50,150)
    g2_amp = PVector(random(40, 90),random(40, 90))
    g2_angle = random(TWO_PI)
    g2_speed = -1*random(.0495,.0505) 
    g2_damp = 1.0
    g2 = Gimbal(g2_pos, g2_amp, angle=g2_angle, speed=g2_speed, damp=g2_damp)
    # hinge 1
    h1_arm1_len = random(250,300)
    h1_arm2_len = random(250,300)
    h1 = Gimbal_Hinge(g2, g1, h1_arm2_len, h1_arm1_len, draw_traj=False)
    
    #################### GIMBAL HINGE 2 #########################
    # gimbal 3
    g3_pos = PVector(width-200, 0)
    g3_amp = PVector(random(40, 90),random(40, 90))
    g3_angle = random(TWO_PI)
    g3_speed = -1*random(.0495,.0505) 
    g3_damp = 1.0
    g3 = Gimbal(g3_pos, g3_amp, angle=g3_angle, speed=g3_speed, damp=g3_damp)
    # gimbal 4
    g4_pos = PVector(width-50,150)
    g4_amp = PVector(random(40, 90),random(40, 90))
    g4_angle =  random(TWO_PI)
    g4_speed = random(.0495,.0505) 
    g4_damp = 1.0
    g4 = Gimbal(g4_pos, g4_amp, angle=g4_angle, speed=g4_speed, damp=g4_damp)
    # hinge 2
    h2_arm1_len = random(250,300)
    h2_arm2_len = random(250,300)
    h2 = Gimbal_Hinge(g3, g4, h2_arm1_len, h2_arm1_len, draw_traj=False)
    
    #################### GIMBAL HINGE 3 #########################
    # gimbal 5
    g5_pos = PVector(500, 0)
    g5_amp = PVector(random(40, 90),random(40, 90))
    g5_angle = random(TWO_PI)
    g5_speed = -1*random(.0495,.0505) 
    g5_damp = 1.0
    g5 = Gimbal(g5_pos, g5_amp, angle=g5_angle, speed=g5_speed, damp=g5_damp)
    # gimbal 6
    g6_pos = PVector(700,0)
    g6_amp = PVector(random(40, 90),random(40, 90))
    g6_angle =  random(TWO_PI)
    g6_speed = random(.0495,.0505) 
    g6_damp = 1.0
    g6 = Gimbal(g6_pos, g6_amp, angle=g6_angle, speed=g6_speed, damp=g6_damp)
    # hinge 3
    h3_arm1_len = random(250,300)
    h3_arm2_len = random(250,300)
    h3 = Gimbal_Hinge(g5, g6, h3_arm1_len, h3_arm1_len, draw_traj=False)
    

    #################### HINGE HINGE 1 #########################
    hh1_arm1_len = random(280,320)
    hh1_arm2_len = random(280,320)
    hh1 = Hinge_Hinge(h3, h2, hh1_arm1_len, hh1_arm2_len)
    
    #################### HINGE HINGE 3 #########################
    hh2_arm1_len = random(380,420)
    hh2_arm2_len = random(380,420)
    hh2 = Hinge_Hinge(h1, hh1, hh2_arm1_len, hh2_arm2_len)

    #################### LINEAR TRAJ #########################
    dir = PVector(0.02,0)
    traj = Linear_Traj(hh2, dir, draw_hinge=True)
    return traj
    
