from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView, UpdateView, DeleteView, CreateView, ListView
from ticket.models import Ticket


class TicketDetailView(DetailView):
    model = Ticket
    template_name = "ticket_detail.html"


class TicketUpdateView(UpdateView):
    model = Ticket
    template_name = "ticket_update.html"
    fields = (
        "organization_name",
        "applicant",
        "priority",
        "type",
        "ticket_name",
        "status",
        "executor"
    )



class TicketDeleteView(DeleteView):
    model = Ticket
    template_name = "ticket_delete.html"
    success_url = reverse_lazy("article_list")


class TicketCreateView(CreateView):
    model = Ticket
    template_name = "ticket_create.html"
    fields = (
        "organization_name",
        "applicant",
        "priority",
        "type",
        "ticket_name",
        "status",
        "executor"

    )


class TicketListView(ListView):
    model = Ticket
    template_name = "ticket_list.html"
