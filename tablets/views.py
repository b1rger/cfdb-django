from django.views.generic.detail import DetailView
from django.shortcuts import render, redirect, get_object_or_404
from .models import Tablet, Glyph, TabletImage, Sign
from .forms import TabletForm, SignForm, GlyphForm, TabletImageForm


class TabletImageDetailView(DetailView):
    model = TabletImage

    def get_context_data(self, **kwargs):
        context = super(TabletImageDetailView, self).get_context_data(**kwargs)
        return context


def create_tabletImg(request):
    if request.method == "POST":
        form = TabletImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('tablets:tabletImg_list')
        else:
            return render(request, 'tablets/create_tabletImg.html', {'form': form})
    else:
        form = TabletImageForm()
        return render(request, 'tablets/create_tabletImg.html', {'form': form})


def edit_tabletImg(request, pk):
    instance = get_object_or_404(TabletImage, id=pk)
    if request.method == "POST":
        form = TabletImageForm(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('tablets:tabletImg_detail', pk=pk)
        else:
            return render(
                request, 'tablets/create_tabletImg.html', {'form': form, 'instance': instance}
            )
    else:
        form = TabletImageForm(instance=instance)
        return render(
            request, 'tablets/create_tabletImg.html', {'form': form, 'instance': instance})


class GlyphDetailView(DetailView):
    model = Glyph

    def get_context_data(self, **kwargs):
        context = super(GlyphDetailView, self).get_context_data(**kwargs)
        return context


def create_glyph(request):
    if request.method == "POST":
        form = GlyphForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('tablets:glyph_list')
        else:
            return render(request, 'tablets/create_glyph.html', {'form': form})
    else:
        form = GlyphForm()
        return render(request, 'tablets/create_glyph.html', {'form': form})


def edit_glyph(request, pk):
    instance = get_object_or_404(Glyph, id=pk)
    if request.method == "POST":
        form = GlyphForm(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('tablets:glyph_detail', pk=pk)
        else:
            return render(
                request, 'tablets/create_glyph.html', {'form': form, 'instance': instance}
            )
    else:
        form = GlyphForm(instance=instance)
        return render(request, 'tablets/create_glyph.html', {'form': form, 'instance': instance})


class SignDetailView(DetailView):
    model = Sign

    def get_context_data(self, **kwargs):
        current_object = self.object
        context = super(SignDetailView, self).get_context_data(**kwargs)
        context['glyph_list'] = Glyph.objects.filter(sign=current_object.id)
        context['glyphs'] = len(context['glyph_list'])
        return context


def create_sign(request):
    if request.method == "POST":
        form = SignForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('tablets:sign_list')
        else:
            return render(request, 'tablets/create_sign.html', {'form': form})
    else:
        form = SignForm()
        return render(request, 'tablets/create_sign.html', {'form': form})


def edit_sign(request, pk):
    instance = get_object_or_404(Sign, id=pk)
    if request.method == "POST":
        form = SignForm(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('tablets:sign_detail', pk=pk)
        else:
            return render(
                request, 'tablets/create_sign.html', {'form': form, 'instance': instance}
            )
    else:
        form = SignForm(instance=instance)
        return render(request, 'tablets/create_sign.html', {'form': form, 'instance': instance})


class TabletDetailView(DetailView):
    model = Tablet

    def get_context_data(self, **kwargs):
        context = super(TabletDetailView, self).get_context_data(**kwargs)
        current_object = self.object
        context['glyph_list'] = Glyph.objects.filter(tablet=current_object.id)
        context['glyphs'] = len(context['glyph_list'])
        context['img_list'] = TabletImage.objects.filter(tablet=current_object.id)
        context['images'] = len(context['img_list'])
        return context


def create_tablet(request):
    if request.method == "POST":
        form = TabletForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('tablets:tablet_list')
        else:
            return render(request, 'tablets/create_tablet.html', {'form': form})
    else:
        form = TabletForm()
        return render(request, 'tablets/create_tablet.html', {'form': form})


def edit_tablet(request, pk):
    instance = get_object_or_404(Tablet, id=pk)
    if request.method == "POST":
        form = TabletForm(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('tablets:tablet_detail', pk=pk)
        else:
            return render(
                request, 'tablets/create_tablet.html', {'form': form, 'instance': instance}
            )
    else:
        form = TabletForm(instance=instance)
        return render(request, 'tablets/create_tablet.html', {'form': form, 'instance': instance})
