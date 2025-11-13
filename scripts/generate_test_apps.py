#!/usr/bin/env python3

"""
Generate test apps with random variations
Creates 1000 apps with different:
- Number of screenshots (1-5)
- Description lengths (short, medium, long)
- Random names and content
"""

import os
import random
import shutil

# Lorem ipsum text for descriptions
LOREM_SHORT = """Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."""

LOREM_MEDIUM = """Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.

Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.

## Features
- Feature one with detailed description
- Feature two with more information
- Feature three with additional details"""

LOREM_LONG = """# Complete Application Guide

## Overview
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.

## Features
- **Advanced Feature One**: Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur
- **Advanced Feature Two**: Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum
- **Advanced Feature Three**: Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium
- **Advanced Feature Four**: Totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo

## Installation
1. Download the latest version from the repository
2. Extract the archive to your preferred location
3. Run the installer and follow the on-screen instructions
4. Launch the application and configure your settings

## Getting Started
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nemo enim ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit, sed quia consequuntur magni dolores eos qui ratione voluptatem sequi nesciunt.

### Step 1: Configuration
Neque porro quisquam est, qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit.

### Step 2: Usage
Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium.

### Step 3: Advanced Options
Totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo.

## Support
If you need assistance, please visit our support portal or contact the development team.

## License
Licensed under the MIT License. See LICENSE file for details.

## Contributing
We welcome contributions from the community. Please read our contributing guidelines before submitting pull requests."""

CHANGELOG_TEMPLATE = """# Changelog

## [1.0.{patch}] - 2023-{month:02d}-{day:02d}
### Added
- New feature implementation for improved functionality
- Enhanced user interface components
- Additional configuration options

### Fixed
- Resolved critical bug affecting performance
- Fixed memory leak in core module
- Corrected display issues on certain devices

### Changed
- Updated dependency versions
- Improved error handling and logging
- Optimized resource usage"""

AUTHORS = [
    "@developer1", "@coder123", "@techguru", "@appmaster", 
    "@devpro", "@codewizard", "@programmer", "@softwaredev",
    "@hackerman", "@builderx", "@designdev", "@fullstack"
]

APP_TYPES = ["tool", "game", "utility", "system", "network", "multimedia", "productivity"]
APP_CATEGORIES = ["Tools", "Games", "Utilities", "System", "Network", "Media", "Office"]

def generate_app(app_number):
    """Generate a single test app"""
    
    app_name = f"testapp{app_number:04d}.app"
    app_dir = os.path.join("apps", app_name)
    
    # Create directory
    os.makedirs(app_dir, exist_ok=True)
    
    # Random variations
    num_screenshots = random.randint(1, 5)
    desc_type = random.choice(['short', 'medium', 'long'])
    author = random.choice(AUTHORS)
    category = random.choice(APP_CATEGORIES)
    app_type = random.choice(APP_TYPES)
    
    # Select description
    if desc_type == 'short':
        description = LOREM_SHORT
    elif desc_type == 'medium':
        description = LOREM_MEDIUM
    else:
        description = LOREM_LONG
    
    # Create DESCRIPTION.md
    with open(os.path.join(app_dir, "DESCRIPTION.md"), 'w') as f:
        f.write(description)
    
    # Create CHANGELOG.md
    changelog = CHANGELOG_TEMPLATE.format(
        patch=random.randint(0, 9),
        month=random.randint(1, 12),
        day=random.randint(1, 28)
    )
    with open(os.path.join(app_dir, "CHANGELOG.md"), 'w') as f:
        f.write(changelog)
    
    # Copy icon (use existing screenshot1.png as template)
    source_icon = "apps/test.app/screenshot1.png"
    if os.path.exists(source_icon):
        for i in range(1, num_screenshots + 1):
            shutil.copy(source_icon, os.path.join(app_dir, f"screenshot{i}.png"))
    
    # Create manifest.yml
    screenshots_yaml = "\n".join([f"  - screenshot{i}.png" for i in range(1, num_screenshots + 1)])
    
    manifest = f"""name: Test App {app_number:04d}
sources:
  type: git
  location:
    origin: https://github.com/test/app{app_number}.git
executionfile:
  type: lua
  location:
    origin: https://raw.githubusercontent.com/and3rson/lilka/refs/heads/main/hardware/v2/main.kicad_pro
short_description: {category} {app_type} for testing - App #{app_number}
description: "@DESCRIPTION.md"
changelog: "@CHANGELOG.md"
author: "{author}"
license: MIT
keira_version: 1.0.0
icon: screenshot1.png
screenshots:
{screenshots_yaml}
"""
    
    with open(os.path.join(app_dir, "manifest.yml"), 'w') as f:
        f.write(manifest)
    
    return app_name

def main():
    print("🚀 Generating 1000 test apps...")
    print("")
    
    # Check if template exists
    if not os.path.exists("apps/test.app/screenshot1.png"):
        print("❌ Error: Template screenshot not found at apps/test.app/screenshot1.png")
        print("Please ensure the test.app exists first")
        return
    
    generated = []
    
    for i in range(1, 101):
        try:
            app_name = generate_app(i)
            generated.append(app_name)
            
            if i % 100 == 0:
                print(f"✓ Generated {i} apps...")
        except Exception as e:
            print(f"❌ Error generating app {i}: {e}")
    
    print("")
    print(f"🎉 Successfully generated {len(generated)} test apps!")
    print("")
    print("Generated apps have:")
    print("  - 1-5 random screenshots per app")
    print("  - Short, medium, or long descriptions")
    print("  - Random authors and categories")
    print("  - Unique changelogs")
    print("")
    print("To build the site with all apps, run:")
    print("  ./scripts/build.site.sh")
    print("")
    print("⚠️  WARNING: Building 1000+ apps will take significant time!")
    print("Consider building only a subset for testing pagination.")

if __name__ == "__main__":
    main()
