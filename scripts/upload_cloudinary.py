import yaml

data = {
    'scene': {
        'ANIMATED_CHARACTERS': [
            {
                'character_cfg': 'examples/garlic_out/char_cfg.yaml',
                'motion_cfg': 'examples/config/motion/jumping.yaml',
                'retarget_cfg': 'examples/config/retarget/fair1_ppf_duo1.yaml'
            },
            {
                'character_cfg': '/home/ajay/Animations/AnimatedDrawings/output/char_cfg.yaml',
                'motion_cfg': '/home/ajay/Animations/AnimatedDrawings/config/motion/Running_Motion.yaml',
                'retarget_cfg': '/home/ajay/Animations/AnimatedDrawings/config/retarget/Running_Retarget.yaml'
            },
            {
                'character_cfg': '/home/ajay/Animations/AnimatedDrawings/examples/characters/char3/char_cfg.yaml',
                'motion_cfg': '/home/ajay/Animations/AnimatedDrawings/config/motion/jumping_jacks.yaml',
                'retarget_cfg': '/home/ajay/Animations/AnimatedDrawings/config/retarget/cmu1_pfp.yaml'
            }
        ]
    },
    'controller': {
        'MODE': 'video_render',
        'OUTPUT_VIDEO_PATH': './video.gif'
    }
}

# Write data to YAML file
with open('config.yaml', 'w') as file:
    yaml.dump(data, file)