# DJ Blog Setup Guide

## Required Packages

The following packages are required for the blog to work properly:

### Python Packages (install with pip)
```bash
pip install -r requirements.txt
```

Or install individually:
```bash
pip install Django>=5.2.3
pip install django-ckeditor>=6.7.0
pip install mysqlclient>=2.2.0
pip install Pillow>=10.0.0
```

### External Dependencies

1. **Tailwind CSS** - Already included via CDN in templates
2. **Font Awesome** - Already included via CDN in templates
3. **MySQL Database** - Make sure MySQL server is running

## Setup Instructions

1. **Install Python packages:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Configure your database** in `djblog/settings.py`:
   - Make sure MySQL server is running
   - Update database credentials if needed

3. **Run migrations:**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

4. **Create a superuser:**
   ```bash
   python manage.py createsuperuser
   ```

5. **Create some sample data** (optional):
   - Go to admin panel at `/admin/`
   - Create categories like: Technology, Lifestyle, Travel, etc.
   - Create tags like: Python, Django, Web Development, etc.

6. **Run the development server:**
   ```bash
   python manage.py runserver
   ```

## Features Included

### Templates with Tailwind CSS
- **Responsive design** - Works on desktop, tablet, and mobile
- **Modern UI components** - Cards, forms, navigation, pagination
- **Component-based system** - Reusable template components
- **Dark mode ready** - Easy to add dark mode support

### Functionality
- **Post management** - Create, read, update, delete posts
- **User authentication** - Login, logout, registration
- **Comments system** - Users can comment on posts
- **Like system** - Users can like/unlike posts
- **Search and filtering** - Search by title, content, category, tags
- **Pagination** - Efficient loading of large post lists
- **Rich text editor** - CKEditor for post content

### Components Created
- `base.html` - Main layout template
- `post_card.html` - Individual post card component
- `search_filter.html` - Search and filter form component
- `pagination.html` - Pagination component
- `post_list.html` - Homepage with all posts
- `post_detail.html` - Individual post view
- `post_create.html` - Create new post form
- `post_update.html` - Edit post form
- `user_login.html` - Login form with logout success message
- `user_register.html` - Registration form

## Customization

### Styling
- Edit `static/css/custom.css` for additional custom styles
- Modify Tailwind config in `base.html` for color schemes
- Update component templates for layout changes

### Features
- Add more fields to Post model (images, publish date, etc.)
- Implement user profiles
- Add email notifications
- Implement SEO features
- Add social media sharing

## Troubleshooting

### Common Issues
1. **Missing packages** - Run `pip install -r requirements.txt`
2. **Database connection** - Check MySQL server and credentials
3. **Static files not loading** - Run `python manage.py collectstatic`
4. **Template not found** - Check `INSTALLED_APPS` includes 'blog'
5. **Logout "Method Not Allowed" error** - Make sure the logout button uses POST method (already fixed in templates)

### Security Features
- **CSRF Protection** - All forms include CSRF tokens
- **Secure Logout** - Logout uses POST method to prevent CSRF attacks
- **Login Required** - Post creation, editing, and deletion require authentication

### Package Versions
Make sure you have compatible versions:
- Python 3.8+
- Django 5.2+
- MySQL 8.0+ or MySQL 5.7+
