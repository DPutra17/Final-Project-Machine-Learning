# Theme Management Guide

## 📁 File Structure

```
src/
├── config/
│   ├── theme.py        # ⭐ Central theme configuration
│   └── settings.py     # App settings (imports theme)
├── utils/
│   └── styling.py      # Apply CSS (uses theme)
└── components/
    └── cards.py        # UI components (uses theme)
```

## 🎨 Theme Configuration (`config/theme.py`)

Semua styling aplikasi diatur dari satu file ini:

### Color Palette
- **Primary Colors**: Purple-Blue gradient
- **Accent Colors**: Pink, Red, Blue, Cyan gradients
- **Background**: White, light gray
- **Text**: Dark gray, medium gray
- **Status**: Success, warning, danger, info

### Typography
- **Font Family**: Poppins
- **Font Weights**: Light (300) - Bold (700)
- **Font Sizes**: xs (0.75rem) - 5xl (3rem)

### Spacing
- **xs**: 0.5rem
- **sm**: 1rem
- **md**: 1.5rem
- **lg**: 2rem
- **xl**: 3rem
- **2xl**: 4rem

### Border Radius
- **sm**: 8px - Small elements
- **md**: 12px - Buttons
- **lg**: 15px - Cards
- **xl**: 20px - Large cards
- **full**: 50px - Pills/Rounded

### Shadows
- **sm**: Subtle shadow
- **md**: Default shadow
- **lg**: Prominent shadow
- **xl**: Deep shadow
- **primary**: Purple shadow
- **primary_hover**: Purple hover shadow

## 🔧 How to Use

### 1. Update Colors
Edit `config/theme.py`:
```python
COLORS = {
    'primary': '#667eea',  # Change this
    'secondary': '#764ba2', # Or this
    # ... other colors
}
```

### 2. Update Typography
```python
TYPOGRAPHY = {
    'font_family': "'YourFont', sans-serif",
    'font_sizes': {
        'base': '1.1rem',  # Increase base font size
    }
}
```

### 3. Update Spacing
```python
SPACING = {
    'md': '2rem',  # More spacing
}
```

### 4. Apply Changes
Changes automatically apply to:
- ✅ All pages
- ✅ All components
- ✅ All UI elements
- ✅ Sidebar
- ✅ Buttons
- ✅ Cards
- ✅ Forms

No need to edit multiple files!

## 📦 Components Using Theme

### Gradient Cards (`components/cards.py`)
Uses: `COLORS`, `BORDER_RADIUS`, `SHADOWS`

### Buttons
Uses: `COLORS['gradient_purple']`, `BORDER_RADIUS['md']`, `SHADOWS['primary']`

### Hero Banner
Uses: `COLORS['bg_hero']`, `BORDER_RADIUS['xl']`

### Metrics
Uses: `COLORS['gradient_purple']` for value text

## 🎯 Best Practices

1. **Always use theme variables** - Don't hardcode colors
2. **Update theme.py only** - Don't edit individual CSS
3. **Test on all pages** - Changes affect entire app
4. **Use semantic names** - `primary`, `success`, not `blue`, `green`
5. **Consistent spacing** - Use SPACING values

## 🚀 Quick Theme Changes

### Change to Blue Theme
```python
COLORS = {
    'primary': '#4facfe',
    'secondary': '#00f2fe',
    'gradient_purple': 'linear-gradient(135deg, #4facfe 0%, #00f2fe 100%)',
}
```

### Change to Green Theme
```python
COLORS = {
    'primary': '#11998e',
    'secondary': '#38ef7d',
    'gradient_purple': 'linear-gradient(135deg, #11998e 0%, #38ef7d 100%)',
}
```

### Increase All Spacing
```python
SPACING = {
    'xs': '0.75rem',  # +0.25rem
    'sm': '1.5rem',   # +0.5rem
    'md': '2rem',     # +0.5rem
    'lg': '2.5rem',   # +0.5rem
    'xl': '3.5rem',   # +0.5rem
}
```

## 📝 Notes

- Theme loads once on app start
- Restart Streamlit to see theme changes
- All CSS is generated from `get_custom_css()` function
- Component styles inherit from theme
- Dark mode support coming soon

---

**Maintenance File**: `src/config/theme.py`  
**Last Updated**: December 2024
