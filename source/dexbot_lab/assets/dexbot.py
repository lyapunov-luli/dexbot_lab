import isaaclab.sim as sim_utils
from isaaclab.actuators import ImplicitActuatorCfg
from isaaclab.assets import ArticulationCfg
from dexbot_lab.assets import DEXBOT_ASSETS_DATA_DIR

##
# Configuration
##

init_pos = (0.0, 0.0, 0.91)

default_joint_angles = {
            'leg_l2_joint': -0.04,
            'leg_l3_joint': -0.12,
            'leg_l1_joint': -0.35,
            'leg_l4_joint': 0.7,
            'leg_l5_joint': -0.4,
            'leg_l6_joint': 0.02,
            'leg_r2_joint': 0.04,
            'leg_r3_joint': 0.12,
            'leg_r1_joint': -0.35,
            'leg_r4_joint': 0.7,
            'leg_r5_joint': -0.4,
            'leg_r6_joint': -0.02,

            'arm_l1_joint': 0.174444,
            'arm_l2_joint': 0.209333,
            'arm_l3_joint': 0.,
            'arm_l4a_joint': -0.43611,
            'arm_l5a_joint': -0.0523,
            'arm_r1_joint': 0.174444,
            'arm_r2_joint': -0.209333,
            'arm_r3_joint': 0.,
            'arm_r4a_joint': -0.4361,
            'arm_r5a_joint': 0.0523,
        }


DEXBOT_CFG = ArticulationCfg(
    spawn=sim_utils.UrdfFileCfg(
        urdf_path=f"{DEXBOT_ASSETS_DATA_DIR}/robot/urdf/HIT02.usd",
        activate_contact_sensors=True,
        rigid_props=sim_utils.RigidBodyPropertiesCfg(
            disable_gravity=False,
            retain_accelerations=False,
            linear_damping=0.0,
            angular_damping=0.0,
            max_linear_velocity=1000.0,
            max_angular_velocity=1000.0,
            max_depenetration_velocity=1.0,
        ),
        articulation_props=sim_utils.ArticulationRootPropertiesCfg(
            enabled_self_collisions=False,
            solver_position_iteration_count=8,
            solver_velocity_iteration_count=4,
        ),
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=init_pos,
        joint_pos=default_joint_angles,
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=1.0,
    actuators={
        "motor": ImplicitActuatorCfg(
            joint_names_expr=[
                'leg_l2_joint',
                'leg_l3_joint',
                'leg_l1_joint',
                'leg_l4_joint',
                'leg_l5_joint',
                'leg_l6_joint',
                'leg_r2_joint',
                'leg_r3_joint',
                'leg_r1_joint',
                'leg_r4_joint',
                'leg_r5_joint',
                'leg_r6_joint',

                'arm_l1_joint',
                'arm_l2_joint',
                'arm_l3_joint',
                'arm_l4a_joint',
                'arm_l5a_joint',
                'arm_r1_joint',
                'arm_r2_joint',
                'arm_r3_joint',
                'arm_r4a_joint',
                'arm_r5a_joint',
            ],
            effort_limit={
                'leg_l2_joint': 360,
                'leg_l3_joint': 360,
                'leg_l1_joint': 120,
                'leg_l4_joint': 360,
                'leg_l5_joint': 120,
                'leg_l6_joint': 120,
                'leg_r2_joint': 360,
                'leg_r3_joint': 360,
                'leg_r1_joint': 120,
                'leg_r4_joint': 360,
                'leg_r5_joint': 120,
                'leg_r6_joint': 120,

                'arm_l1_joint': 120,
                'arm_l2_joint': 120,
                'arm_l3_joint': 120,
                'arm_l4a_joint': 120,
                'arm_l5a_joint': 120,
                'arm_r1_joint': 120,
                'arm_r2_joint': 120,
                'arm_r3_joint': 120,
                'arm_r4a_joint': 120,
                'arm_r5a_joint': 120,
            },
            velocity_limit={
                'leg_l2_joint': 10,
                'leg_l3_joint': 10,
                'leg_l1_joint': 10,
                'leg_l4_joint': 10,
                'leg_l5_joint': 10,
                'leg_l6_joint': 10,
                'leg_r2_joint': 10,
                'leg_r3_joint': 10,
                'leg_r1_joint': 10,
                'leg_r4_joint': 10,
                'leg_r5_joint': 10,
                'leg_r6_joint': 10,

                'arm_l1_joint': 10,
                'arm_l2_joint': 10,
                'arm_l3_joint': 10,
                'arm_l4a_joint': 10,
                'arm_l5a_joint': 10,
                'arm_r1_joint': 10,
                'arm_r2_joint': 10,
                'arm_r3_joint': 10,
                'arm_r4a_joint': 10,
                'arm_r5a_joint': 10,
            },
            stiffness={
                    'leg_l2_joint': 200,
                     'leg_l1_joint': 350.0,
                     'leg_l3_joint': 200.0,
                     'leg_l4_joint': 350.0,
                     'leg_l5_joint': 30,
                     'leg_l6_joint': 15,
                     'leg_r2_joint': 200.0,
                     'leg_r1_joint': 350.0,
                     'leg_r3_joint': 200.0,
                     'leg_r4_joint': 350.0,
                     'leg_r5_joint': 30,
                     'leg_r6_joint': 15,
                     'arm_l1_joint': 180.,
                     'arm_l2_joint': 180.,
                     'arm_l3_joint': 90.,
                     'arm_l4a_joint': 90.,
                     'arm_l5a_joint': 90.,
                     'arm_r1_joint': 180.,
                     'arm_r2_joint': 180.,
                     'arm_r3_joint': 90.,
                     'arm_r4a_joint': 90.,
                     'arm_r5a_joint': 90.
            },
            damping={
                    'leg_l2_joint': 7,
                   'leg_l1_joint': 7,
                   'leg_l3_joint': 7,
                   'leg_l4_joint': 7,
                   'leg_l5_joint': 7,
                   'leg_l6_joint': 7,
                   'leg_r2_joint': 7,
                   'leg_r1_joint': 7,
                   'leg_r3_joint': 7,
                   'leg_r4_joint': 7,
                   'leg_r5_joint': 7,
                   'leg_r6_joint': 7,
                   'arm_l1_joint': 7.,
                   'arm_l2_joint': 7.,
                   'arm_l3_joint': 7.,
                   'arm_l4a_joint': 7.,
                   'arm_l5a_joint': 7.,
                   'arm_r1_joint': 7.,
                   'arm_r2_joint': 7.,
                   'arm_r3_joint': 7.,
                   'arm_r4a_joint': 7.,
                   'arm_r5a_joint': 7.
            },
            armature={
                'leg_l2_joint': 0.01,
                'leg_l3_joint': 0.01,
                'leg_l1_joint': 0.01,
                'leg_l4_joint': 0.01,
                'leg_l5_joint': 0.01,
                'leg_l6_joint': 0.01,
                'leg_r2_joint': 0.01,
                'leg_r3_joint': 0.01,
                'leg_r1_joint': 0.01,
                'leg_r4_joint': 0.01,
                'leg_r5_joint': 0.01,
                'leg_r6_joint': 0.01,

                'arm_l1_joint': 0.01,
                'arm_l2_joint': 0.01,
                'arm_l3_joint': 0.01,
                'arm_l4a_joint': 0.01,
                'arm_l5a_joint': 0.01,
                'arm_r1_joint': 0.01,
                'arm_r2_joint': 0.01,
                'arm_r3_joint': 0.01,
                'arm_r4a_joint': 0.01,
                'arm_r5a_joint': 0.01,
            },
        ),
    },
)

"""Configuration for the dexbot robot with simplified collision meshes."""


DEXBOT_FIXED_CFG = DEXBOT_CFG.copy()
DEXBOT_FIXED_CFG.spawn.articulation_props = sim_utils.ArticulationRootPropertiesCfg(
    enabled_self_collisions=False,
    fix_root_link=True,
)
DEXBOT_FIXED_CFG.init_state = ArticulationCfg.InitialStateCfg(
    pos=(0.0, 0.0, 1.0),
    joint_pos=default_joint_angles,
    joint_vel={".*": 0.0},
)
"""Configuration for the dexbot with fixed root link."""
