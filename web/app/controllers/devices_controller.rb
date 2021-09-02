class DevicesController < ApplicationController

  def edit
    load_device
    build_device
  end

  def update
    load_device
    build_device
    save_device or render 'edit'
  end

  private
  
  def build_device
    @device ||= device_scope.build
    @device.attributes = device_params
  end

  def save_device
    @device.random_weights = params[:device][:random_weights].to_json
    @device.random_durations = params[:device][:random_durations].transform_values(&:to_f).to_json
    if @device.save
      redirect_to edit_device_path(@device)
    end
  end

  def device_params
    device_params = params[:device]
    device_params ? device_params.permit(:current_animation, :animation_strategy) : {}
  end
  
  def load_device
    @device = Device.find(params[:id])
  end
  
  def device_scope
    
  end

end