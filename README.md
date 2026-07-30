# Telegram Desktop — Accessibility Tracker

This repository tracks **accessibility improvements** in [Telegram Desktop](https://github.com/telegramdesktop/tdesktop). Each release corresponds to an official Telegram Desktop version that introduced new accessibility features for screen reader users.

> This is **not** a separate build. All changes listed here are merged into the official Telegram Desktop and its dependencies ([lib_ui](https://github.com/desktop-app/lib_ui), [lib_base](https://github.com/desktop-app/lib_base), [patches](https://github.com/desktop-app/patches)).

## Releases

| Version | Type | Accessibility Changes |
|---|---|---|
| [v6.2.5](https://github.com/rezabakhshilaktasaraei/tdesktop-accessible/releases/tag/v6.2.5) | Pre-release | First accessibility support — infrastructure, core widget roles/names, screen reader detection |
| [v6.2.6](https://github.com/rezabakhshilaktasaraei/tdesktop-accessible/releases/tag/v6.2.6) | Pre-release | Value API for sliders, Checkbox & Radiobutton keyboard navigation |
| [v6.3.0](https://github.com/rezabakhshilaktasaraei/tdesktop-accessible/releases/tag/v6.3.0) | Stable | Checkbox state change notification fix |
| [v6.3.2](https://github.com/rezabakhshilaktasaraei/tdesktop-accessible/releases/tag/v6.3.2) | Stable | SideBarButton announces unread badge count |
| [v6.3.6](https://github.com/rezabakhshilaktasaraei/tdesktop-accessible/releases/tag/v6.3.6) | Stable | UIAutomation Invoke support for buttons and checkboxes |
| [v6.3.7](https://github.com/rezabakhshilaktasaraei/tdesktop-accessible/releases/tag/v6.3.7) | Stable | Chat filters sidebar fully accessible as tab list |
| [v6.4.0](https://github.com/rezabakhshilaktasaraei/tdesktop-accessible/releases/tag/v6.4.0) | Stable | SettingsButton toggles report checked/unchecked state |
| [v6.5.0](https://github.com/rezabakhshilaktasaraei/tdesktop-accessible/releases/tag/v6.5.0) | Stable | Accessibility labels for history view buttons |
| [v6.6.0](https://github.com/rezabakhshilaktasaraei/tdesktop-accessible/releases/tag/v6.6.0) | Stable | Screen reader support for menus, `Accessible::Item` infrastructure for painted elements, accessible name for the search button in narrow layout |
| [v6.6.4](https://github.com/rezabakhshilaktasaraei/tdesktop-accessible/releases/tag/v6.6.4) | Stable | `ButtonMenu` role for main menu buttons |
| [v6.7.7](https://github.com/rezabakhshilaktasaraei/tdesktop-accessible/releases/tag/v6.7.7) | Stable | Screen reader support for the country select box and the language list |
| [v6.8.3](https://github.com/rezabakhshilaktasaraei/tdesktop-accessible/releases/tag/v6.8.3) | Stable | Screen reader support for the chat list and the message list |
| [v6.9.4](https://github.com/rezabakhshilaktasaraei/tdesktop-accessible/releases/tag/v6.9.4) | Beta | Chat folders strip exposed as an accessible list, chat-list type-to-search redirection, restored Home/End navigation in the chat list, screen reader focus/activate on chat list rows |
| [v7.0.1](https://github.com/rezabakhshilaktasaraei/tdesktop-accessible/releases/tag/v7.0.1) | Stable | Screen reader focus/activate on country, language, and message history rows; keyboard message selection with multi-selection state; chat list focused on launch; main-menu hit-area hidden from screen readers |
| [v7.0.2](https://github.com/rezabakhshilaktasaraei/tdesktop-accessible/releases/tag/v7.0.2) | Stable | Keep the message list visible and focused while a chat loads |

## All Merged Pull Requests

### Telegram Desktop ([telegramdesktop/tdesktop](https://github.com/telegramdesktop/tdesktop))

<!-- prs:tdesktop:start -->
| PR | Title | Author | First Release |
|---|---|---|---|
| [#29808](https://github.com/telegramdesktop/tdesktop/pull/29808) | Introduce initial accessibility support to Telegram Desktop | [@rezabakhshilaktasaraei](https://github.com/rezabakhshilaktasaraei) | v6.2.5 |
| [#29964](https://github.com/telegramdesktop/tdesktop/pull/29964) | Accessibility: Add Value API, improve Slider, and refine Roles | [@rezabakhshilaktasaraei](https://github.com/rezabakhshilaktasaraei) | v6.2.6 |
| [#30022](https://github.com/telegramdesktop/tdesktop/pull/30022) | Make chat filters sidebar accessible to screen readers | [@rezabakhshilaktasaraei](https://github.com/rezabakhshilaktasaraei) | v6.3.7 |
| [#30213](https://github.com/telegramdesktop/tdesktop/pull/30213) | Accessibility: add labels for buttons history | [@mukthar777](https://github.com/mukthar777) | v6.5.0 |
| [#30340](https://github.com/telegramdesktop/tdesktop/pull/30340) | Add accessible name to search button in narrow layout | [@rezabakhshilaktasaraei](https://github.com/rezabakhshilaktasaraei) | v6.6.0 |
| [#30445](https://github.com/telegramdesktop/tdesktop/pull/30445) | feat(accessibility): use ButtonMenu role for main menu buttons | [@rezabakhshilaktasaraei](https://github.com/rezabakhshilaktasaraei) | v6.6.4 |
| [#30303](https://github.com/telegramdesktop/tdesktop/pull/30303) | Add screen reader support for country select box | [@rezabakhshilaktasaraei](https://github.com/rezabakhshilaktasaraei) | v6.7.7 |
| [#30304](https://github.com/telegramdesktop/tdesktop/pull/30304) | Add screen reader support for language list | [@rezabakhshilaktasaraei](https://github.com/rezabakhshilaktasaraei) | v6.7.7 |
| [#30305](https://github.com/telegramdesktop/tdesktop/pull/30305) | Add screen reader support for chat list | [@rezabakhshilaktasaraei](https://github.com/rezabakhshilaktasaraei) | v6.8.3 |
| [#30306](https://github.com/telegramdesktop/tdesktop/pull/30306) | Add screen reader support for message list | [@rezabakhshilaktasaraei](https://github.com/rezabakhshilaktasaraei) | v6.8.3 |
| [#30758](https://github.com/telegramdesktop/tdesktop/pull/30758) | Engage chat search on typing instead of focus in screen reader mode | [@rezabakhshilaktasaraei](https://github.com/rezabakhshilaktasaraei) | v6.9.4 |
| [#30762](https://github.com/telegramdesktop/tdesktop/pull/30762) | Redirect chat list typing to the search field in screen reader mode | [@rezabakhshilaktasaraei](https://github.com/rezabakhshilaktasaraei) | v6.9.4 |
| [#30772](https://github.com/telegramdesktop/tdesktop/pull/30772) | Expose chat folders strip as an accessible tab control | [@rezabakhshilaktasaraei](https://github.com/rezabakhshilaktasaraei) | v6.9.4 |
| [#30879](https://github.com/telegramdesktop/tdesktop/pull/30879) | Expose the chat-folders strip as an accessible list | [@rezabakhshilaktasaraei](https://github.com/rezabakhshilaktasaraei) | v6.9.4 |
| [#30886](https://github.com/telegramdesktop/tdesktop/pull/30886) | Restore Home/End navigation in the chat list | [@rezabakhshilaktasaraei](https://github.com/rezabakhshilaktasaraei) | v6.9.4 |
| [#30769](https://github.com/telegramdesktop/tdesktop/pull/30769) | Support screen reader focus and activate on chat list rows | [@rezabakhshilaktasaraei](https://github.com/rezabakhshilaktasaraei) | v6.9.4 |
| [#30930](https://github.com/telegramdesktop/tdesktop/pull/30930) | Focus chat list on launch in screen reader mode | [@rezabakhshilaktasaraei](https://github.com/rezabakhshilaktasaraei) | v7.0.1 |
| [#30931](https://github.com/telegramdesktop/tdesktop/pull/30931) | Hide the main menu hit-area button from screen readers | [@rezabakhshilaktasaraei](https://github.com/rezabakhshilaktasaraei) | v7.0.1 |
| [#30940](https://github.com/telegramdesktop/tdesktop/pull/30940) | Support screen reader focus and activate on country list rows | [@rezabakhshilaktasaraei](https://github.com/rezabakhshilaktasaraei) | v7.0.1 |
| [#30943](https://github.com/telegramdesktop/tdesktop/pull/30943) | Support screen reader focus and activate on language list rows | [@rezabakhshilaktasaraei](https://github.com/rezabakhshilaktasaraei) | v7.0.1 |
| [#30948](https://github.com/telegramdesktop/tdesktop/pull/30948) | Support screen reader focus and activate on message history rows | [@rezabakhshilaktasaraei](https://github.com/rezabakhshilaktasaraei) | v7.0.1 |
| [#30947](https://github.com/telegramdesktop/tdesktop/pull/30947) | Add keyboard message selection for screen reader users | [@rezabakhshilaktasaraei](https://github.com/rezabakhshilaktasaraei) | v7.0.1 |
| [#30958](https://github.com/telegramdesktop/tdesktop/pull/30958) | Report multi-selection state on message history lists | [@rezabakhshilaktasaraei](https://github.com/rezabakhshilaktasaraei) | v7.0.1 |
| [#30975](https://github.com/telegramdesktop/tdesktop/pull/30975) | Keep the message list visible and focused while a chat loads | [@rezabakhshilaktasaraei](https://github.com/rezabakhshilaktasaraei) | v7.0.2 |
<!-- prs:tdesktop:end -->

### lib_ui ([desktop-app/lib_ui](https://github.com/desktop-app/lib_ui))

<!-- prs:lib_ui:start -->
| PR | Title | Author | First Release |
|---|---|---|---|
| [#265](https://github.com/desktop-app/lib_ui/pull/265) | Add accessibility roles, names, and keyboard activation for core widgets | [@rezabakhshilaktasaraei](https://github.com/rezabakhshilaktasaraei) | v6.2.5 |
| [#268](https://github.com/desktop-app/lib_ui/pull/268) | Add keyboard navigation and accessibility state handling for Checkbox and Radiobutton | [@rezabakhshilaktasaraei](https://github.com/rezabakhshilaktasaraei) | v6.2.6 |
| [#270](https://github.com/desktop-app/lib_ui/pull/270) | Add pressed state reporting for AbstractButton and fix Checkbox state notification | [@rezabakhshilaktasaraei](https://github.com/rezabakhshilaktasaraei) | v6.3.0 |
| [#271](https://github.com/desktop-app/lib_ui/pull/271) | Revert pressed state reporting from AbstractButton | [@rezabakhshilaktasaraei](https://github.com/rezabakhshilaktasaraei) | v6.3.0 |
| [#272](https://github.com/desktop-app/lib_ui/pull/272) | Add accessibility name for SideBarButton with badge support | [@rezabakhshilaktasaraei](https://github.com/rezabakhshilaktasaraei) | v6.3.2 |
| [#275](https://github.com/desktop-app/lib_ui/pull/275) | Add UIAutomation Invoke support for buttons and checkboxes | [@rezabakhshilaktasaraei](https://github.com/rezabakhshilaktasaraei) | v6.3.6 |
| [#277](https://github.com/desktop-app/lib_ui/pull/277) | Report checked state for SettingsButton toggles | [@rezabakhshilaktasaraei](https://github.com/rezabakhshilaktasaraei) | v6.4.0 |
| [#278](https://github.com/desktop-app/lib_ui/pull/278) | Add Accessible::Item for exposing painted (non-QWidget) elements to screen readers | [@rezabakhshilaktasaraei](https://github.com/rezabakhshilaktasaraei) | v6.6.0 |
| [#284](https://github.com/desktop-app/lib_ui/pull/284) | Accessibility: Add screen reader support for Menu items | [@rezabakhshilaktasaraei](https://github.com/rezabakhshilaktasaraei) | v6.6.0 |
| [#286](https://github.com/desktop-app/lib_ui/pull/286) | Accessibility: Improve menu accessibility states and navigation | [@rezabakhshilaktasaraei](https://github.com/rezabakhshilaktasaraei) | v6.6.0 |
| [#292](https://github.com/desktop-app/lib_ui/pull/292) | feat(accessibility): add ButtonMenu role to IconButton and SideBarButton | [@rezabakhshilaktasaraei](https://github.com/rezabakhshilaktasaraei) | v6.6.4 |
| [#293](https://github.com/desktop-app/lib_ui/pull/293) | Restore menu item focus for accessibility, fix DropdownMenu | [@rezabakhshilaktasaraei](https://github.com/rezabakhshilaktasaraei) | v6.6.4 |
| [#308](https://github.com/desktop-app/lib_ui/pull/308) | Let ElasticScroll pass unhandled keys to the parent | [@rezabakhshilaktasaraei](https://github.com/rezabakhshilaktasaraei) | v6.9.4 |
| [#304](https://github.com/desktop-app/lib_ui/pull/304) | feat(accessibility): support PageTab role and selected state on buttons | [@rezabakhshilaktasaraei](https://github.com/rezabakhshilaktasaraei) | v6.9.4 |
| [#311](https://github.com/desktop-app/lib_ui/pull/311) | Use List/ListItem accessibility role for ordered button strips | [@rezabakhshilaktasaraei](https://github.com/rezabakhshilaktasaraei) | v6.9.4 |
| [#303](https://github.com/desktop-app/lib_ui/pull/303) | feat(accessibility): support SetFocus and Press actions on painted list items | [@rezabakhshilaktasaraei](https://github.com/rezabakhshilaktasaraei) | v6.9.4 |
| [#319](https://github.com/desktop-app/lib_ui/pull/319) | Add multi-select fields to AccessibilityState | [@rezabakhshilaktasaraei](https://github.com/rezabakhshilaktasaraei) | v7.0.1 |
<!-- prs:lib_ui:end -->

### lib_base ([desktop-app/lib_base](https://github.com/desktop-app/lib_base))

<!-- prs:lib_base:start -->
| PR | Title | Author | First Release |
|---|---|---|---|
| [#273](https://github.com/desktop-app/lib_base/pull/273) | Add screen reader detection via QAccessible::ActivationObserver | [@rezabakhshilaktasaraei](https://github.com/rezabakhshilaktasaraei) | v6.2.5 |
<!-- prs:lib_base:end -->

### patches ([desktop-app/patches](https://github.com/desktop-app/patches))

<!-- prs:patches:start -->
| PR | Title | Author | First Release |
|---|---|---|---|
| [#233](https://github.com/desktop-app/patches/pull/233) | Use RTTI to get class name for accessibility | [@ilya-fedin](https://github.com/ilya-fedin) | v6.2.5 |
| [#245](https://github.com/desktop-app/patches/pull/245) | Add patch: fix toggle state notification for all checkable widgets | [@rezabakhshilaktasaraei](https://github.com/rezabakhshilaktasaraei) | v6.6.0 |
| [#253](https://github.com/desktop-app/patches/pull/253) | Don't require an action interface for UIA SelectionContainer *(later reverted by [#258](https://github.com/desktop-app/patches/pull/258))* | [@rezabakhshilaktasaraei](https://github.com/rezabakhshilaktasaraei) | v6.9.4 |
| [#254](https://github.com/desktop-app/patches/pull/254) | Backport UIA selection + orientation interfaces for custom tab controls | [@rezabakhshilaktasaraei](https://github.com/rezabakhshilaktasaraei) | v6.9.4 |
| [#257](https://github.com/desktop-app/patches/pull/257) | Use RTTI in automation id on Qt 5, too (accessibility commit within "Fixes") | [@ilya-fedin](https://github.com/ilya-fedin) | v6.9.4 |
| [#258](https://github.com/desktop-app/patches/pull/258) | Revert "Don't require an action interface for UIA SelectionContainer" (no longer needed — see note below) | [@rezabakhshilaktasaraei](https://github.com/rezabakhshilaktasaraei) | v7.0.1 |
<!-- prs:patches:end -->

### NVDA ([nvaccess/nvda](https://github.com/nvaccess/nvda))

Some issues can also be fixed on the screen reader side. The change below addresses the same root cause as [patches#253](https://github.com/desktop-app/patches/pull/253), from within NVDA itself.

<!-- prs:nvda:start -->
| PR | Title | Author | First Release |
|---|---|---|---|
| [#20255](https://github.com/nvaccess/nvda/pull/20255) | fix: handle COMError in UIA selectionContainer to prevent silent focus | [@rezabakhshilaktasaraei](https://github.com/rezabakhshilaktasaraei) | NVDA 2026.3 |
<!-- prs:nvda:end -->

> **Silent focus on selected list items — how it was resolved.** On Qt 5.15, the UIA `SelectionContainer` provider errors when an accessible item exposes no action interface (as Telegram Desktop's chat rows once did), which made NVDA go silent when focusing a *selected* row. It was first worked around with a downstream Qt patch ([patches#253](https://github.com/desktop-app/patches/pull/253), shipped in **v6.9.4**). Since then the chat-list items expose a press action ([lib_ui#303](https://github.com/desktop-app/lib_ui/pull/303)), so the provider passes the check naturally and the patch was reverted as no longer needed ([patches#258](https://github.com/desktop-app/patches/pull/258), **v7.0.1**). NVDA 2026.3 ([nvda#20255](https://github.com/nvaccess/nvda/pull/20255)) adds defense-in-depth for older Telegram builds or other Qt apps that still hit the error.

## Contributors

- **[@rezabakhshilaktasaraei](https://github.com/rezabakhshilaktasaraei)** (Reza Bakhshi Laktasaraei) — initiated accessibility support in Telegram Desktop; authored 44 of 47 merged PRs across tdesktop, lib_ui, lib_base, and patches, plus the NVDA-side fix [nvda#20255](https://github.com/nvaccess/nvda/pull/20255).
- **[@ilya-fedin](https://github.com/ilya-fedin)** (Ilya Fedin) — RTTI-based class name and automation id for accessibility ([patches#233](https://github.com/desktop-app/patches/pull/233), [patches#257](https://github.com/desktop-app/patches/pull/257)).
- **[@mukthar777](https://github.com/mukthar777)** (K H Musthafal Mukthar) — added accessibility labels for history view buttons ([tdesktop#30213](https://github.com/telegramdesktop/tdesktop/pull/30213)).

## Tested With

- [NVDA](https://www.nvaccess.org/) on Windows
- [Windows Narrator](https://support.microsoft.com/en-us/windows/complete-guide-to-narrator-e4397a0d-ef4f-b386-d8ae-c172f109bdb1)

## License

The source code is published under GPLv3 with OpenSSL exception, same as the official [Telegram Desktop](https://github.com/telegramdesktop/tdesktop). See [LICENSE](https://github.com/telegramdesktop/tdesktop/blob/dev/LICENSE) for details.
