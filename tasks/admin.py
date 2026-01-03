from django.contrib import admin as django_admin
from unfold.admin import ModelAdmin
from django.utils.html import format_html
from django.utils.translation import gettext_lazy as _
from django.db.models import QuerySet
from django.http import HttpRequest

from .models import Task


@django_admin.register(Task)
class TaskAdmin(ModelAdmin):  # Changed from admin.ModelAdmin to unfold.admin.ModelAdmin
    """
    Administration avancée pour le modèle Task.
    Optimisée pour la productivité et l'ergonomie.
    """
    
    # ============================================================
    # AFFICHAGE DE LA LISTE
    # ============================================================
    
    list_display = (
        "id",
        "title_with_icon",
        "status_badge",
        "description_preview",
        "formatted_created_at",
        "quick_actions",
    )
    
    list_display_links = ("id", "title_with_icon")
    
    list_filter = (
        "is_done",
        "created_at",
    )
    
    search_fields = (
        "title",
        "description",
    )
    
    ordering = ("-created_at",)
    
    list_per_page = 25
    
    # ============================================================
    # ORGANISATION DES CHAMPS (ÉDITION)
    # ============================================================
    
    fieldsets = (
        (_("📝 Informations principales"), {
            "fields": ("title", "description"),
            "description": "Définissez le titre et la description de votre tâche.",
        }),
        (_("✅ Statut"), {
            "fields": ("is_done",),
            "description": "Marquez la tâche comme terminée ou en cours.",
        }),
        (_("📅 Métadonnées"), {
            "fields": ("created_at_display",),
            "classes": ("collapse",),
            "description": "Informations de création (automatiques).",
        }),
    )
    
    readonly_fields = ("created_at_display",)
    
    # ============================================================
    # MÉTHODES PERSONNALISÉES POUR L'AFFICHAGE
    # ============================================================
    
    @django_admin.display(description="Tâche", ordering="title")
    def title_with_icon(self, obj: Task) -> str:
        """Affiche le titre avec une icône selon le statut."""
        icon = "✅" if obj.is_done else "⏳"
        return format_html(
            '<span style="font-weight: 600;">{} {}</span>',
            icon,
            obj.title
        )
    
    @django_admin.display(description="Statut", ordering="is_done")
    def status_badge(self, obj: Task) -> str:
        """Affiche un badge coloré pour le statut."""
        if obj.is_done:
            return format_html(
                '<span style="'
                'background: linear-gradient(135deg, #10b981 0%, #059669 100%);'
                'color: white;'
                'padding: 4px 12px;'
                'border-radius: 12px;'
                'font-size: 11px;'
                'font-weight: 600;'
                'text-transform: uppercase;'
                'letter-spacing: 0.5px;'
                'box-shadow: 0 2px 4px rgba(16, 185, 129, 0.3);'
                '">✓ Terminé</span>'
            )
        else:
            return format_html(
                '<span style="'
                'background: linear-gradient(135deg, #f59e0b 0%, #d97706 100%);'
                'color: white;'
                'padding: 4px 12px;'
                'border-radius: 12px;'
                'font-size: 11px;'
                'font-weight: 600;'
                'text-transform: uppercase;'
                'letter-spacing: 0.5px;'
                'box-shadow: 0 2px 4px rgba(245, 158, 11, 0.3);'
                '">⏳ En cours</span>'
            )
    
    @django_admin.display(description="Aperçu")
    def description_preview(self, obj: Task) -> str:
        """Affiche un aperçu tronqué de la description."""
        if obj.description:
            preview = obj.description[:60]
            if len(obj.description) > 60:
                preview += "..."
            return format_html(
                '<span style="color: #6b7280; font-style: italic;">{}</span>',
                preview
            )
        return format_html(
            '<span style="color: #d1d5db; font-style: italic;">Aucune description</span>'
        )
    
    @django_admin.display(description="Date de création", ordering="created_at")
    def formatted_created_at(self, obj: Task) -> str:
        """Affiche la date de création formatée avec icône."""
        return format_html(
            '<span style="color: #4b5563;">📅 {}</span>',
            obj.created_at.strftime("%d/%m/%Y à %H:%M")
        )
    
    @django_admin.display(description="Actions rapides")
    def quick_actions(self, obj: Task) -> str:
        """Affiche des boutons d'action rapide."""
        if obj.is_done:
            button_text = "Réouvrir"
            button_color = "#f59e0b"
            icon = "↩️"
        else:
            button_text = "Terminer"
            button_color = "#10b981"
            icon = "✓"
        
        return format_html(
            '<a href="#" onclick="return false;" style="'
            'background: {};'
            'color: white;'
            'padding: 4px 10px;'
            'border-radius: 6px;'
            'font-size: 11px;'
            'font-weight: 500;'
            'text-decoration: none;'
            'display: inline-block;'
            '">{} {}</a>',
            button_color,
            icon,
            button_text
        )
    
    @django_admin.display(description="Date de création")
    def created_at_display(self, obj: Task) -> str:
        """Affiche la date de création complète (readonly)."""
        if obj.created_at:
            return obj.created_at.strftime("%d/%m/%Y à %H:%M:%S")
        return "-"
    
    # ============================================================
    # ACTIONS PERSONNALISÉES
    # ============================================================
    
    actions = [
        "mark_as_done",
        "mark_as_pending",
        "duplicate_tasks",
    ]
    
    @django_admin.action(description="✅ Marquer comme terminé")
    def mark_as_done(self, request: HttpRequest, queryset: QuerySet[Task]) -> None:
        """Marque les tâches sélectionnées comme terminées."""
        updated = queryset.update(is_done=True)
        self.message_user(
            request,
            f"{updated} tâche(s) marquée(s) comme terminée(s).",
            level="SUCCESS"
        )
    
    @django_admin.action(description="⏳ Marquer comme en cours")
    def mark_as_pending(self, request: HttpRequest, queryset: QuerySet[Task]) -> None:
        """Marque les tâches sélectionnées comme en cours."""
        updated = queryset.update(is_done=False)
        self.message_user(
            request,
            f"{updated} tâche(s) marquée(s) comme en cours.",
            level="SUCCESS"
        )
    
    @django_admin.action(description="📋 Dupliquer les tâches sélectionnées")
    def duplicate_tasks(self, request: HttpRequest, queryset: QuerySet[Task]) -> None:
        """Duplique les tâches sélectionnées."""
        count = 0
        for task in queryset:
            task.pk = None  # Crée une nouvelle instance
            task.title = f"{task.title} (copie)"
            task.is_done = False  # Les copies sont en cours par défaut
            task.save()
            count += 1
        
        self.message_user(
            request,
            f"{count} tâche(s) dupliquée(s) avec succès.",
            level="SUCCESS"
        )
    
    # ============================================================
    # AMÉLIORATION DE L'EXPÉRIENCE UTILISATEUR
    # ============================================================
    
    def get_queryset(self, request: HttpRequest) -> QuerySet[Task]:
        """Optimise les requêtes pour éviter les N+1."""
        qs = super().get_queryset(request)
        # Ajoutez select_related/prefetch_related si nécessaire
        return qs
    
    class Media:
        """Personnalisation CSS/JS optionnelle."""
        css = {
            'all': ('admin/css/custom_admin.css',)  # Optionnel
        }
