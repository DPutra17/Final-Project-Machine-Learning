# Theme Version 2.0 - Modern & Sophisticated

## 🎨 Design Philosophy

Tema baru ini menggunakan pendekatan **modern, minimal, dan sophisticated** dengan fokus pada:
- **Clean aesthetics** - Layout yang bersih dan tidak berlebihan
- **Professional look** - Cocok untuk presentasi dan production
- **Better readability** - Typography dan spacing yang optimal
- **Smooth interactions** - Animasi halus dengan cubic-bezier easing

## 🎯 Key Changes

### Color Palette
- **Primary**: Deep Blue (#2563eb → #7c3aed) - Modern dan professional
- **Success**: Emerald (#10b981) - Fresh dan vibrant
- **Info**: Cyan (#06b6d4) - Clean dan calming
- **Warning**: Amber (#f59e0b) - Clear attention
- **Danger**: Rose (#f43f5e) - Modern red

### Typography
- **Font**: Inter (dari Poppins) - More modern, better readability
- **Weight**: 300-800 range untuk hierarchy yang jelas
- **Letter spacing**: -0.02em untuk headings (lebih tight, modern look)

### Shadows
- **Elevation system**: xs, sm, md, lg, xl, 2xl
- **Softer shadows**: Multiple layer shadows untuk depth yang natural
- **Card shadows**: Dedicated card elevation untuk consistency

### Border Radius
- **Scale**: xs (4px) sampai 3xl (24px)
- **Modern scale**: Lebih terukur dan konsisten

### Components

#### Cards
- **Feature Cards**: White background, subtle shadow, colored top border on hover
- **Gradient Cards**: Modern gradients dengan better shadow system
- **Hover effects**: Smooth transform dengan scale effect

#### Buttons
- **Primary**: Gradient blue-purple dengan modern shadow
- **Hover**: Smooth lift effect (translateY + scale)
- **Active state**: Proper press feedback

#### Forms
- **Input fields**: Rounded corners, subtle border, focus ring effect
- **Focus state**: Blue ring dengan smooth transition
- **Better padding**: More comfortable input area

#### Navigation (Sidebar)
- **Modern pills**: Transparent default, gradient when active
- **Smooth hover**: translateX effect dengan color change
- **Minimal design**: Clean dan tidak ramai

#### Tabs
- **Segmented control**: Modern iOS-style tabs
- **Background**: Subtle gray dengan white active state
- **No borders**: Cleaner look

#### Dataframes
- **Modern table**: Better spacing, uppercase headers
- **Hover effect**: Row highlight on hover
- **Border system**: Clean borders dengan primary accent

#### Alerts
- **Gradient backgrounds**: Subtle gradients dengan strong left border
- **Better colors**: Pastel backgrounds dengan dark text
- **Icons**: Implicit dengan color coding

## 📐 Spacing System

- Block padding: 2rem 1rem 4rem
- Card padding: 2rem (reduced dari 2.5rem)
- Gap between columns: "medium"
- Margin system: Consistent spacing throughout

## 🎭 Animation System

- **Fast**: 0.15s ease - Micro interactions
- **Normal**: 0.3s ease - Standard interactions
- **Easing**: cubic-bezier(0.4, 0, 0.2, 1) - Smooth natural motion

## 🌟 Best Practices

1. **Use semantic colors**: success, warning, danger, info
2. **Consistent spacing**: Follow the spacing scale
3. **Elevation hierarchy**: Use shadow scale appropriately
4. **Smooth transitions**: Always add transition for hover states
5. **Accessibility**: Maintain color contrast ratios

## 🔧 Customization

Tema ini fully centralized di `src/config/theme.py`. Untuk mengubah:

```python
COLORS = {
    'primary': '#2563eb',  # Change this for different primary color
    # ...
}

SHADOWS = {
    'card': '...',  # Adjust shadow intensity
    # ...
}
```

## 📱 Responsive Design

- Max width: 1200px untuk better readability
- Column gaps: Menggunakan "medium" spacing
- Card layout: Automatically responsive dengan st.columns()

## 🚀 Performance

- CSS variables: Faster rendering
- Minimal shadows: Better performance
- Optimized transitions: GPU-accelerated transforms

## 💡 Tips

- Gunakan gradient cards untuk highlight features
- Feature cards untuk navigation/CTA
- Metric cards otomatis styled dengan gradient text
- Tabs menggunakan segmented control style
- Alerts dengan gradient backgrounds
